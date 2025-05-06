from flask import Blueprint, render_template

titulos = Blueprint('titulos', __name__, template_folder='templates')

@titulos.route('/')
def index():
    return render_template('public/titulos.html')
