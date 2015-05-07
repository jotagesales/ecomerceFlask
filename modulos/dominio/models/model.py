# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey
from default.engine import Base, session
from modulos.dominio import TABLE_PREFIX
__author__ = 'Jotage'

class UF(Base):
    __tablename__ = TABLE_PREFIX + 'uf'

    id = Column(Integer, primary_key= True)
    sigla = Column(String(2), nullable= False, unique= True)
    nome = Column(String(60), nullable= False)

    def __init__(self, pId, pSigla, pNome):
        self.id = pId
        self.sigla = pSigla
        self.nome = pNome

    @staticmethod
    def qtde_uf():
        return session.query(UF).count()

class Municipio(Base):
    __tablename__ = TABLE_PREFIX + 'municipio'

    __ref_id_uf = '%s.%s' %(UF.__tablename__, UF.id.description)

    id = Column(Integer, primary_key= True)
    id_uf = Column(Integer, ForeignKey(__ref_id_uf))
    nome = Column(String(60), nullable= False)

    def __init__(self, pId, pIdUF, pNome):
        self.id = pId
        self.id_uf = pIdUF
        self.nome = pNome

    @staticmethod
    def qtde_municipios():
        return session.query(Municipio).count()

    @staticmethod
    def get_all():
        """
        método responsável por litar todos os municipios
        :rtype : lista de tuplas
        """
        total_registros = Municipio.qtde_municipios()
        lst_registros = session.query(Municipio.id, Municipio.nome, UF.sigla)\
                                                    .join(UF)\
                                                    .all()
        return lst_registros, total_registros

    @staticmethod
    def get_municipio_uf(pIdUf):
        """

        :rtype : retorna lista de municipios filtrados por uf
        """
        idUf = int(pIdUf)
        return session.query(Municipio.id, Municipio.nome).filter_by(id_uf = idUf ).all()
