from flask import Blueprint

ping = Blueprint('ping', __name__)

@ping.route('/')
def index():
    return "ping"
