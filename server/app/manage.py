import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.database import db
from config import get_config
import app


app_config = get_config()
app.config.from_object(app_config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()