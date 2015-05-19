# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String

from default.engine import Object_persistent
from modulos.seguranca import TABLE_PREFIX


__author__ = 'Jotage'

class Usuario(Object_persistent):
    __tablename__ = TABLE_PREFIX + 'usuario'


    id_usuario = Column(Integer,primary_key= True)
    login = Column(String, nullable= False, unique= True)
    senha = Column(String, nullable= False )
    email = Column(String(100), nullable= False)
    perfil = Column(Integer, nullable= False)
