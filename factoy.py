from flask import Flask
from config  import  Config
from api.user.views import user_api
from api.home.views import home_api
from api.products.views import product_api
from api.markets.views import market_api
from api.sales.views import sales_api

# from middleware.auth import auth_api_v1
from config import db

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True,template_folder='templates')
    app.config.from_object(Config)
    app.register_blueprint(user_api)
    app.register_blueprint(home_api)
    app.register_blueprint(product_api)
    app.register_blueprint(market_api)
    app.register_blueprint(sales_api)
    db.init_app(app)
    return app
