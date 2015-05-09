# coding=utf-8
from flask import Blueprint, redirect, render_template, url_for, request, session, jsonify, session

from modulos.seguranca.controller.controller import SegurancaController


__author__ = 'Jotage'

#blueprint 
bp_area_interna = Blueprint('areainterna',__name__, url_prefix='/areainterna')

#objeto controller do back end de seguranca
server_seguranca = SegurancaController()

@bp_area_interna.route('/', methods=['GET'])
def home():
    return render_template('area_interna/area_interna.html')

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
        try:
            server_seguranca.addUsuario(pLogin= login,
                                        pSenha= senha,
                                        pEmail= email,
                                        pPerfil= perfil,
                                        pUsuarioLog= session['usuario_logado']
                                        )
            return jsonify(),201
        except Exception as error:
            pass
    return render_template('area_interna/area_interna.html')