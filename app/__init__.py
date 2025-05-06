from flask import Flask
from app.home.routes import home
from app.estadio.routes import estadio
from app.ping.routes import ping
from app.titulos.routes import titulos

# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = (("/ping", ping), ("/", home), ("/estadio", estadio), ("/titulos", titulos))

def create_app():
    app = Flask(__name__)
    
    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)


    return app