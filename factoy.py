from flask import Flask
from config  import  Config
from api.user.views import user_api
# from middleware.auth import auth_api_v1
from config import db

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True,template_folder='templates')
    app.config.from_object(Config)
    app.register_blueprint(user_api)
    db.init_app(app)
    return app
