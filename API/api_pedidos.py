from flask.blueprints import Blueprint
from flask.templating import render_template

__author__ = 'Jotage'

bp_pedidos = Blueprint('pedidos', __name__)

@bp_pedidos.route('/')
def home():
    return render_template('front_end/front_end.html')