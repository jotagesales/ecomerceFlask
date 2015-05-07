# coding=utf-8
from flask.blueprints import Blueprint
from flask.templating import render_template

__author__ = 'Jotage'

bp_area_interna = Blueprint('templates_area_interna',__name__, url_prefix='/areainterna/')

@bp_area_interna.route('/', methods=['GET', 'POST'])
def area_interna():
    return render_template('area_interna/area_interna.html')