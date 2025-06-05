import os

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_BASE_PATH = os.path.join(APP_ROOT, "logs")

os.makedirs(LOG_BASE_PATH, exist_ok=True)

APP_LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s in %(module)s: %(message)s'
        }
    },
    'handlers': {
        'app': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_BASE_PATH, "app.log")
        },
        'selenium': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_BASE_PATH, "selenium.log")
        },
    },
    'loggers': {
        'app': {
            'handlers': ['app'],
            'level': 'INFO',
            'formatter': 'verbose',
            'propagate': True,
        },
        'selenium': {
            'handlers': ['selenium'],
            'level': 'INFO',
            'formatter': 'verbose',
            'propagate': True,
        },
    }
}
