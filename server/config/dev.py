from datetime import timedelta

from config import config

class Config(config.Config):
    DEBUG = True
    APP_URL = 'http://127.0.0.1:5000'
    APP_NAME = "Instagram & Twitter bot"
    SECRET_KEY = "My_Secret_Key"
    SQLALCHEMY_DATABASE_URI = "postgresql://shebang:shebang@postgres:5432/only_fans_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False