# coding=utf-8
import uuid
from flask import Flask

from API.api_area_interna import bp_area_interna
from API.api_pedidos import bp_pedidos
from default.engine import create_all_tables_database
from modulos.seguranca.controller.controller import SegurancaController


app = Flask(__name__)
#configurndo a aplicacao
app.session_cookie_name = 'session_pedidos'
app.secret_key = str(uuid.uuid4())

#registraondo os blueprints
app.register_blueprint(bp_area_interna)
app.register_blueprint(bp_pedidos)


if __name__ == '__main__':
    create_all_tables_database()
    SegurancaController().configuraUsuarioAdministrador()
    app.run( debug= True)
