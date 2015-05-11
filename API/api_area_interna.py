# coding=utf-8
from flask import Blueprint, redirect, render_template, url_for, request, session, jsonify, session

from modulos.seguranca.controller.controller import SegurancaController
from modulos.seguranca.models import PERFIL

__author__ = 'Jotage'

#blueprint 
bp_area_interna = Blueprint('areainterna',__name__, url_prefix='/areainterna')

#objeto controller do back end de seguranca
server_seguranca = SegurancaController()

@bp_area_interna.route('/', methods=['GET'])
def home():
    return render_template('area_interna/dasboard.html')

@bp_area_interna.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.json.get('username')
        senha = request.json.get('password')
        
        #verificando se o usuário é valido
        id_usuario, user_is_valid = server_seguranca.verifica_usuario(login, senha)
        if user_is_valid:
            session['id_usuario_logado'] = id_usuario
            return jsonify(mensagem='Login efetuado com sucesso'), 200
        else:
            return jsonify(mensagem= 'Usuário ou senha inválidos'), 401
    
    return render_template('login.html')
    
    
@bp_area_interna.route('/logout', methods=['GET'])
def logout():
    session.pop('id_usuario_logado')
    return redirect(url_for('areainterna.login'))


@bp_area_interna.route('/cadastroUsuario', methods=['GET', 'POST'])
def cadastroUsuario():
    if request.method == 'POST':
        login = request.json.get('login')
        senha = request.json.get('senha')
        email = request.json.get('email')
        perfil= request.json.get('perfil')
        usuario_logado = session.get('id_usuario_logado')
        try:
            server_seguranca.addUsuario(pLogin= login,
                                        pSenha= senha,
                                        pEmail= email,
                                        pPerfil= perfil,
                                        pUsuarioLog= usuario_logado
                                        )
            return jsonify(msg='registro salvo'),201
        except Exception as error:
            return jsonify(msg= error.message),400
    return render_template('area_interna/cad_usuario.html')
 
@bp_area_interna.route('/consultaUsuarios')
def consultaUsuarios():
    usuarios = []
    for usuario in  server_seguranca.consultaUsuarios():
        usuarios.append({'login':usuario.login,
                         'email': usuario.email,
                         'perfil':PERFIL[usuario.perfil]
                        })
    return jsonify(items = usuarios)
    
@bp_area_interna.route('/consultaPerfil')
def consultaPerfil():
    perfis =[]
    for i in PERFIL.keys():
        perfis.append({'codigo':i, 'descricao': PERFIL[i]})
    return jsonify(items = perfis)