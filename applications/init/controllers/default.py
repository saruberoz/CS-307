# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

@auth.requires_login()
def shopping():
    items = db(db.shopping_list).select()
    return dict(items=items)

def recipe():
    recipe = db(db.recipe.id==request.args(0)).select() or redirect(URL('index'))
    user = db(db.auth_user.id==recipe[0].user).select() or redirect(URL('index'))
    ingredients = db(db.ingredient.recipe==recipe[0].id).select()
    comments = db(db.comment.recipe==recipe[0].id).select()
    if auth.user_id > 0:
        collections = db(db.collection.user==auth.user.id).select(db.collection.ALL)
        form=SQLFORM(db.comment)
        form.vars.recipe = recipe[0].id
        if form.accepts(request,session):
            #response.flash = 'form accepted'
            redirect(str(recipe[0].id))
        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill the form'
    else:
        form=""
        collections=""
    if(recipe[0].private and (recipe[0].user.id != auth.user_id)):
        redirect(URL('index'))
    return dict(recipe=recipe[0],user=user[0],form=form,comments=comments, collections=collections, ingredients=ingredients)

@auth.requires_login()
def create_recipe():
    form=SQLFORM(db.recipe)
    if form.accepts(request,session):
        i=1
        while i <= int(request.post_vars['ing_count']):
            ingredient = db(db.ingredientName.name.lower()==request.post_vars['ing_name'+str(i)].lower()).select(db.ingredientName.id).first()
            if ingredient == None:
                db.ingredientName.insert(name=request.post_vars['ing_name'+str(i)])
                ingredient = db(db.ingredientName.name.lower()==request.post_vars['ing_name'+str(i)].lower()).select(db.ingredientName.id).first()
            db.ingredient.insert(quantity=request.post_vars['quantity'+str(i)], unit=request.post_vars['uom'+str(i)], ingredient=ingredient.id, recipe=form.vars.id)
            i=i+1
        response.flash = 'form accepted'
        redirect(URL('recipe', args=[form.vars.id]))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)

@auth.requires_login()
def edit_recipe():
    record = db.recipe(request.args(0)) or redirect(URL('index'))
    ingredients = db(db.ingredient.recipe==record.id).select()
    if(record.user.id != auth.user_id):
        redirect(URL('index'))
    form = SQLFORM(db.recipe, record,wrietable=True,showid=False,deletable=True)
    if form.accepts(request,session):
        i=1
        while i <= int(request.post_vars['ing_count']):
            if request.post_vars['ing_id'+str(i)] == '':
                if request.post_vars['del_ind'+str(i)] != 'delete':
                    ingredient = db(db.ingredientName.name.lower()==request.post_vars['ing_name'+str(i)].lower()).select(db.ingredientName.id).first()
                    if ingredient == None:
                        db.ingredientName.insert(name=request.post_vars['ing_name'+str(i)])
                        ingredient = db(db.ingredientName.name.lower()==request.post_vars['ing_name'+str(i)].lower()).select(db.ingredientName.id).first()
                    db.ingredient.insert(quantity=request.post_vars['quantity'+str(i)], unit=request.post_vars['uom'+str(i)], ingredient=ingredient.id, recipe=form.vars.id)
            elif request.post_vars['del_ind'+str(i)] == 'delete':
                db(db.ingredient.id==request.post_vars['ing_id'+str(i)]).delete()
            else:
                db(db.ingredient.id==request.post_vars['ing_id'+str(i)]).update(quantity=request.post_vars['quantity'+str(i)], unit=request.post_vars['uom'+str(i)])
            i=i+1
        response.flash = 'form accepted'
        redirect(URL('recipe', args=[form.vars.id]))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form, ingredients=ingredients)

@auth.requires_login()
def add_to_collection():
    if (request.args(0) != None) & (request.args(1) != None):
        count = db((db.collection_recipes.collection==request.args(1)) & (db.collection_recipes.recipe==request.args(0))).count()
        if count == 0:
            db.collection_recipes.insert(collection=request.args(1), recipe=request.args(0))
        redirect(URL('collection', args=[request.args(1)]))
    elif request.args(0) != None:
        redirect(URL('recipe/'+request.args(0)))
    else:
        redirect(URL('search'))
    return

def search():
    # kevin h - pagination
    results = 5
    title = ""
    tot_count = 0;

    tot_count = len(db(db.recipe).select())

    #using get vars now, so it does not mess with the <super>/<sub>/etc... heirarchy
    if 'p' in request.vars:
        page = int(request.vars['p'])
    else:
        page = 0

    upper_limit = (page+1)*results + 1
    lower_limit = page * results

    if request.vars.q != None:
        recipes = db(((db.recipe.private == False) | (db.recipe.user == auth.user_id)) & (db.recipe.name.contains(request.vars.q))).select(db.recipe.ALL, limitby=(lower_limit, upper_limit))
        tot_count = len(db(db.recipe.name.contains(request.vars.q)).select(db.recipe.ALL))
        title = "Results for '"+request.vars.q+"':"
    elif request.args(0)== "recent":
        recipes = db((db.recipe.private == False) | (db.recipe.user == auth.user_id)).select(orderby=~db.recipe.id, limitby=(lower_limit, upper_limit))
        print "\n" + db._lastsql + "\n"
        title = "Browse by Most Recent:"
    elif request.args(0)== "prep_time":
        recipes = db((db.recipe.private == False) | (db.recipe.user == auth.user_id)).select(orderby=~db.recipe.prep_time, limitby=(lower_limit, upper_limit))
        title = "Browse by Prep Time:"
    elif request.args(0)== "cook_time":
        recipes = db((db.recipe.private == False) | (db.recipe.user == auth.user_id)).select(orderby=~db.recipe.cook_time, limitby=(lower_limit, upper_limit))
        title = "Browse by Cook Time:"
    elif request.args(0)== "category":
        recipes = db(((db.recipe.private == False) | (db.recipe.user == auth.user_id)) & (db.recipe.category==db(db.category.url_str==request.args(1)).select().first())).select(db.recipe.ALL, orderby=~db.recipe.category, limitby=(lower_limit, upper_limit))
        tot_count = len(db(db.recipe.category==db(db.category.url_str==request.args(1)).select().first()).select(db.recipe.ALL, orderby=~db.recipe.category))
        title = db(db.category.url_str==request.args(1)).select().first().name+":"
    else:
        recipes = db((db.recipe.private == False) | (db.recipe.user == auth.user_id)).select(db.recipe.ALL, limitby=(lower_limit, upper_limit))
        title = "Showing all recipes."

    #print "args: " + str(request.args)
    #print "vars: " + str(request.vars)
    #print "total: " + str(tot_count)
    #print "page: " + str(page)
    #print "length of results: " + str(len(recipes))
    #print "\n"

    #TODO: remove page numbers from args in urls after it is verified that it works in vars
    #      and make args=request.args
    if page > 0:
        prev = A('Previous', _href=URL(r=request, args=request.args, vars=dict(p = (page-1) ) ))
    else:
        prev = A()


    if len(recipes) > results :
        next = A('Next', _href=URL(r = request, args=request.args, vars=dict(p = (page+1) )))
    else:
        next = A()

    # pass it everything!!!
    return dict(recipes = recipes, prev = prev, next = next, results = results, tot_count = tot_count, page = page, browse_title = title, type=request.args(0))

@auth.requires_login()
def collection():
    # add a collection for the user
    if request.vars.name != None:
        db.collection.insert(name=request.vars.name)
        redirect(request.env.http_referer) # send them back from whence they came
    elif request.vars.d == '1':  # deletes the item from the collection
        if (request.vars.c_id != None) & (request.vars.r_id != None):
            db((db.collection_recipes.collection==request.vars.c_id) & (db.collection_recipes.recipe==request.vars.r_id)).delete()
            redirect(URL('default','collection',args=[request.vars.c_id]))
        elif (request.vars.c_id != None):
            db(db.collection_recipes.collection==request.vars.c_id).delete()
            db(db.collection.id==request.vars.c_id).delete()
            redirect(URL('default','collection'))
    elif request.vars.a == '1':  # adds collection to shopping list
        if (request.vars.c_id != None):
            recipes = db((db.collection_recipes.collection==request.vars.c_id) & (db.recipe.id==db.collection_recipes.recipe)).select(db.recipe.id)
            for recipe in recipes:
                ingredients = db(db.ingredient.recipe==recipe).select(db.ingredient.id)
                for ingredient in ingredients:
                    db.shopping_list.update_or_insert(ingredient=ingredient)
            redirect(URL('default','shopping'))

    collections = db(db.collection.user==auth.user.id).select(db.collection.ALL)
    if(request.args(0)):
        collection = db(db.collection.id==request.args(0)).select(db.collection.ALL).first()
    else:
        collection = collections.first()
    if collection:
        collection_id = collection.id
    else:
        collection_id = 0
    recipes = db((db.collection_recipes.collection==collection_id) & (db.recipe.id==db.collection_recipes.recipe)).select(db.recipe.ALL)
    return dict(collections=collections, recipes=recipes, prev="", next="", id=collection_id)

def rating():
    recipe = db(db.recipe.id==request.vars.recipe).select().first()
    if recipe.rating == None:
         rating = db.rating.insert(count=1,value=request.vars.value)
         db(db.recipe.id==recipe.id).update(rating=rating)
    else:
        count=recipe.rating.count
        value = 0.0
        value = recipe.rating.value*count*1.0 + int(float(request.vars.value))*1.0
        count= count + 1
        value = value/count
        db(db.rating.id==recipe.rating.id).update(value=value,count=count)
        if(request.vars.auth == 0):
            csd=d;
    redirect(URL('recipe',args=[request.vars.recipe]))


def test():
    m = "Hello **world** [[link http://web2py.com]]"
    from markmin2html import markmin2html
    return request.args(0)

def error():
    return dict()
