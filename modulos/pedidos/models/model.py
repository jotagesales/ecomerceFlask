# -*- coding:utf-8 -*-

from sqlalchemy import Integer, String, Column, DECIMAL, Boolean ,ForeignKey

from default.engine import Object_persistent

from modulos.pedidos import TABLE_PREFIX
from modulos.seguranca.models import CLIENTE
from modulos.seguranca.models.model import Usuario


__author__ = 'Jotage'

class Cliente(Usuario):
    __tablename__ = TABLE_PREFIX + 'cliente'

    __ref_id_usuario = '{0}.{1}'.format(Usuario.__tablename__, Usuario.id_usuario.description)

    id_cliente = Column(Integer, primary_key= True)
    nome = Column(String(100), nullable= False)
    documento = Column(String(14), nullable= False)
    usuario_id = Column(Integer, ForeignKey(__ref_id_usuario))
    
class UnidadeMedida(Object_persistent):
    __tablename__ = TABLE_PREFIX + 'unidadeMedida'
    
    id_un_medida = Column(Integer,primary_key= True)
    descricao    = Column(String(60), nullable= False)
    
class Produto(Object_persistent):
    __tablename__ = TABLE_PREFIX + 'produto'
    
    __ref_id_un_medida = '{0}.{1}'.format(UnidadeMedida.__tablename__, UnidadeMedida.id_un_medida.description)
    
    id_produto = Column(Integer, primary_key= True)
    descricao  = Column(String(100), nullable= False)
    preco_custo= Column(DECIMAL(10,2))
    preco_venda= Column(DECIMAL(10,2))
    ativo      = Column(Boolean, default= True)
    id_un_medida = Column(Integer, ForeignKey(__ref_id_un_medida))
    



