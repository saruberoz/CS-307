from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Recipedia'
settings.subtitle = 'A recipe storage and sharing app'
settings.author = 'CS 307 Programmers Anonymous'
settings.author_email = 'recipedia.mailer@gmail.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '688a4e12-0139-4490-9e2b-7ba1c50e9979'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
