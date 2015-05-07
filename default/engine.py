# -*- coding: utf-8 -*-

__author__ = 'jotage'

"""
Módulo responsável por fornecer uma engine de banco de dados
que será usada em todo o sistema.
"""
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, DateTime

from default.configuracoes import TIPO_BANCO, DRIVE_CONEXAO,USUARIO, SENHA, HOST, PORTA ,DATABASE


Base = declarative_base()


conectionString = '%s+%s://%s:%s@%s:%s/%s' %(TIPO_BANCO, DRIVE_CONEXAO, USUARIO, SENHA, HOST, PORTA ,DATABASE)

#realizando a conexão com banco de dados
engine = create_engine(conectionString, echo= False)

DbSession = sessionmaker(bind= engine)
session = DbSession()

class Object_persistent(Base):

     __abstract__ = True

     usuario_log = Column(Integer ,nullable= False)
     data_hora = Column(DateTime ,nullable= False, default= datetime.now())

def create_all_tables_database():
    """
    Importar aqui todas as classes models de todos os módulos para que seja criada a tabela no banco de dados
    da respectiva classe
    """
    try:
        print 'Verificando tabelas no banco de dados'

        from modulos.pedidos.models.model import Cliente
        from modulos.dominio.models.model import Municipio, UF
        from modulos.seguranca.models.model import Usuario

        Base.metadata.create_all(engine)

        from modulos.dominio.tabelas.importacao_tabelas import importacao_municipio,importacao_uf
        importacao_uf()
        importacao_municipio()
    except Exception as e:
        raise

