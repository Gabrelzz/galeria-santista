from flask import Blueprint, render_template

estadio = Blueprint('estadio', __name__, template_folder='templates')

@estadio.route('/')
def index():
    return render_template('public/estadio.html')
