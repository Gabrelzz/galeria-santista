from flask import Flask
from app.home import home
from app.estadio import estadio
from app.ping import ping
from app.titulos import titulos

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