from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from models import db
from app import create_app

class CreateDatabase(Command):
    """
    Creates the database based on models.py
    """

    def run(self):
        with create_app().app_context():
            db.create_all()

app_ = create_app()

app_.config.from_pyfile('config.py')
try:
  app_.config.from_pyfile('local_config.py')
except IOError:
  pass

migrate = Migrate(app_, db)
manager = Manager(app_)

manager.add_command('db', MigrateCommand)
manager.add_command('createdb', CreateDatabase())

if __name__ == '__main__':
    manager.run()
