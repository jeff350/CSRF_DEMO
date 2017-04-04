import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

FLASK_DEBUG_DISABLE_STRICT = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False
SECRET_KEY = 'ahdsvgiouywsdboiuywshgo hweb89yhbwoeiughfvuiywegh78h8ogwhe8'
