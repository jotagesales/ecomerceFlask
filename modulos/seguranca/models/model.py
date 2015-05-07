# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash

from default.engine import Object_persistent, session
from modulos.seguranca import TABLE_PREFIX
from modulos.seguranca.models import ADMINISTRADOR


__author__ = 'Jotage'

class Usuario(Object_persistent):
    __tablename__ = TABLE_PREFIX + 'usuarios'


    id_usuario = Column(Integer,primary_key= True)
    login = Column(String, nullable= False, unique= True)
    email = Column(String(100), nullable= False)
    senha = Column(String, nullable= False )
    tipo_usuario = Column(Integer, nullable= False)

    def __init__(self, pLogin='', pEmail='', pSenha='', pTipo_usuario= ADMINISTRADOR, pUsuarioLog= None):
        self.login = pLogin
        self.email = pEmail
        self.senha = generate_password_hash(pSenha)
        self.tipo_usuario = pTipo_usuario
        self.usuario_log = pUsuarioLog


    def __init__(self):
        pass

