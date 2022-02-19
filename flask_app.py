import os
from flask_migrate import Migrate
from application import create_app, db


environment = os.environ.get('FLASK_ENV', 'default')
app = create_app(environment)
migration = Migrate(app, db)
