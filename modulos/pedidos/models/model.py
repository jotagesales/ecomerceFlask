# -*- coding:utf-8 -*-

from sqlalchemy import Integer, String, Column, ForeignKey
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

    def __init__(self, pNome, pDocumento, pEmail):
        super(Cliente, self).__init__(pDocumento, pEmail, CLIENTE)
        self.nome = pNome
        self.documento = pDocumento

if __name__ == '__main__':
    from default.engine import session
    cliente = Cliente('Jose Geraldo ', '12345678909', 'jotage_sales@hotmail.com')

    session.add(cliente)
    session.commit()

