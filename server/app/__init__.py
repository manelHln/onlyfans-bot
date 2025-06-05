import os
import logging.config

from flask import Flask

from services.insta_service import Instagram
from config import logger, get_config

instagram = Instagram()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def create_app():
    app = Flask(__name__)
    
    # Logging configuration
    logging.config.dictConfig(logger.APP_LOG_CONFIG)
    
    #Load app config
    app_config = get_config()
    app.config.from_object(app_config)
    app.config['APP_ROOT'] = APP_ROOT
        
    return app

app = create_app()

@app.route("/")
def hello_world():
    title = instagram.register()
    app.logger.info(title)
    return f"this is the result {title}"

if __name__ == "__main__":
    app.run(debug=True)
