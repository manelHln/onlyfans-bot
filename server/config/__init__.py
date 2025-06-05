import os

def get_config():
    env = os.environ.get('FLASK_ENV', 'dev')

    if env == 'prod':
        from config.prod import Config
        return Config
    else:
        from config.dev import Config
        return Config
