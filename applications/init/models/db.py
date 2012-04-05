# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

if not request.env.web2py_runtime_gae:     
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite') 
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore') 
    ## store sessions and tickets there
    session.connect(request, response, db = db) 
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key()) 
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables

########################################
db.define_table('auth_user',
    Field('username', type='string',
          label=T('Username')),
    Field('first_name', type='string',
          label=T('First Name')),
    Field('last_name', type='string',
          label=T('Last Name')),
    Field('email', type='string',
          label=T('Email')),
    Field('password', type='password',
          readable=False,
          label=T('Password')),
    Field('created_on','datetime',default=request.now,
          label=T('Created On'),writable=False,readable=False),
    Field('modified_on','datetime',default=request.now,
          label=T('Modified On'),writable=False,readable=False,
          update=request.now),
    Field('registration_key',default='',
          writable=False,readable=False),
    Field('reset_password_key',default='',
          writable=False,readable=False),
    Field('registration_id',default='',
          writable=False,readable=False),
    format='%(username)s',
    migrate=settings.migrate)


db.auth_user.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.password.requires = CRYPT(key=auth.settings.hmac_key)
db.auth_user.username.requires = IS_NOT_IN_DB(db, db.auth_user.username)
db.auth_user.registration_id.requires = IS_NOT_IN_DB(db, db.auth_user.registration_id)
db.auth_user.email.requires = (IS_EMAIL(error_message=auth.messages.invalid_email),
                               IS_NOT_IN_DB(db, db.auth_user.email))
auth.define_tables(migrate = settings.migrate) 

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'recipedia.mailer@gmail.com'
mail.settings.login = 'recipedia.mailer:cs307purdue'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
#from gluon.contrib.login_methods.rpx_account import use_janrain
#use_janrain(auth,filename='private/janrain.key')
# *** NOTE: Janrain is already configured for Recipedia.  Just uncomment the lines.

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login

db.define_table('category',
    Field('name',type='string'),
    Field('url_str', type='string'),
    format='%(name)s')

db.define_table('rating',
    Field('count',type='integer',default=0),
    Field('value',type='double',default=0))
    
db.define_table('users_ratings',
    Field('user',db.auth_user),
    Field('rating',db.rating),
    Field('user_rating',type='double'))

db.define_table('collection',
    Field('user',db.auth_user, default=lambda:auth.user.id, writable=False, readable=False),
    Field('name',type='string'))

db.define_table('ingredientName',
    Field('name',type='string'),
    format='%(name)s')

db.define_table('recipe',
    Field('name',type='string'),
    Field('cook_time',type='integer'),
    Field('prep_time',type='integer'),
    Field('ingredients',type='text'),
    Field('directions',type='text'),
    Field('user',db.auth_user, default=lambda:auth.user.id, writable=False, readable=False),
    Field('category',db.category),
    Field('created_on','datetime',default=request.now, label=T('Created On'), writable=False, readable=False),
    Field('modified_on','datetime',default=request.now, label=T('Modified On'),writable=False,readable=False, update=request.now),
    Field('image', 'upload',label=T('Image')),
    Field('video', type='string',label=T('Video   http://www.youtube.com/watch?v=')),
    Field('private',type='boolean',label=T('Private?')),
    Field('rating',db.rating, writable=False, readable=False),
    format='%(name)s')

db.define_table('ingredient',
    Field('quantity', type='double'),
    Field('unit',type='string'),
    Field('ingredient',db.ingredientName),
    Field('recipe', db.recipe),
    format='%(quantity)s %(unit)s %(ingredient.name)s %(recipe.name)s')

db.define_table('collection_recipes',
    Field('collection',db.collection),
    Field('recipe',db.recipe))

db.define_table('shopping_list',
    Field('checked',type='boolean'),
    Field('ingredient',db.ingredient))

db.define_table('comment',
    Field('recipe',db.recipe, readable=False, writable=False),
    Field('user', db.auth_user, default=lambda:auth.user.id, writable=False, readable=False),
    Field('date','datetime',default=request.now, label=T('Created On'), writable=False, readable=False),
    Field('content',type='text', label='Comment'))   
    


#db.define_table('ingedient',
#    Field('count',type='double'),
#    Field('recipe',db.recipe))
