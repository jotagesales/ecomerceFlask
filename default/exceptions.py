# -*- coding: UTF-8 -*-
__author__ = 'Jotage'

class SGC_Exception(Exception):

    def __init__(self):
        self.nome_campo = ''
        self.codigo_erro = 0


class Preenchimento_Invalido(SGC_Exception):

    def __init__(self, nomeCampo):
        self.codigo_erro = 1000
        self.nome_campo = nomeCampo
        self.message = u'O campo {0} está com preenchimento inválido'.format(self.nome_campo)


class Preenchimento_Obrigatorio(SGC_Exception):

    def __init__(self, nomeCampo):
        self.codigo_erro = 1200
        self.nome_campo = nomeCampo
        self.message = u'O campo {0} é de preenchimento obrigatório'.format(self.nome_campo)


class Duplicidade_Registro(SGC_Exception):

    def __init__(self, nomeCampo):
        self.codigo_erro = 1300
        self.nome_campo = nomeCampo
        self.message = u'Registro duplicado, já existe um cadastro para o campo {0}'.format(self.nome_campo)

class Registro_nao_encontrado(SGC_Exception):
    def __init__(self, nomeCampo):
        self.codigo_erro = 1400
        self.nome_campo = nomeCampo
        self.message = u'Não foi encontrado nenhum registro com as informações de {0}'.format(self.nome_campo)

class Registro_referenciado(SGC_Exception):
    def __init__(self, nomeRegistroReferenciado):
        self.codigo_erro = 1500
        self.message = 'Existem {0} referenciado(s) ' \
                       'para esse registro que você está tentando excluir, portanto ' \
                       'não é possível realizar a exclusão'.format(nomeRegistroReferenciado)