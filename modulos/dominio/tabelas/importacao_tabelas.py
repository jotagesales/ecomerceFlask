# -*- coding: UTF-8 -*-

__author__ = 'jotage'

import os
from sqlalchemy.exc import IntegrityError

from modulos.dominio.models.model import UF, Municipio
from default.engine import session


path = os.path.dirname(__file__) + '/'

def importacao_uf():
    """
    importacao da tabela de uf do IBGE
    """

    if UF.qtde_uf() == 0:
        print 'importando tabela de UF'
        arquivo_uf = path + 'UF.txt'
        lst_uf = []
        if os.path.exists(arquivo_uf):
            with open(arquivo_uf) as file_uf:
                for linha in file_uf.readlines():
                    informacoes = linha.split('|')
                    id = informacoes[0].strip()
                    sigla = informacoes[1].strip()
                    nome = informacoes[2]

                    if informacoes[0].isdigit():
                        uf = UF(id, sigla, nome)
                        lst_uf.append(uf)

            try:
                #adicionando todos de uma vez por questao de performace
                session.add_all(lst_uf)
                session.commit()
            except IntegrityError: #realiza a importacao da tabela na primeira vez que roda
                session.rollback()
                pass
            except Exception as e:
                session.rollback()
        else:
            raise Exception(u'Arquivo de UF não encontrado')

def importacao_municipio():
    """
    importacao da tabela de uf do IBGE
    """
    if Municipio.qtde_municipios() == 0:
        print 'importando tabela de Municípios'
        path_municipios = path + 'Municipios.txt'

        lst_municipios = []
        if os.path.exists(path_municipios):
            with open(path_municipios) as file_uf:
                for linha in file_uf.readlines():
                    id_uf = linha[0:2].strip()
                    id_municipio = linha[3:11].strip()
                    nome_municipio = linha[17::].strip()

                    municipio = Municipio(id_municipio, id_uf, nome_municipio)
                    lst_municipios.append(municipio)

            try:
                session.add_all(lst_municipios)
                session.commit()
            except IntegrityError:
                session.rollback()
            except Exception as e:
                session.rollback()
                raise Exception(str(e))

        else:
            raise Exception(u'Arquivo de municípios não encontrado')
