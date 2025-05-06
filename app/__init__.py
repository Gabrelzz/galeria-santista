from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from app.home import home
from app.estadio import estadio
from app.ping import ping
from app.titulos import titulos
from app.auth import auth

from app.models import db, User

login_manager = LoginManager()
bcrypt = Bcrypt()

login_manager.login_view = "auth.login"
login_manager.blueprint_login_views = "info"

# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = (("/ping", ping), ("/", home), ("/estadio", estadio), ("/titulos", titulos), ("auth", auth))

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret_key"
    app.config["SQLALCHEMY_DATABASE_URI" ] = "sqlite:///site.db"
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Usar /endpoint e /endpoint/ é válido.
    app.url_map.strict_slashes = False

    # Registrar cada blueprint ativo
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))