# coding: utf-8
from werkzeug.security import generate_password_hash

from default.engine import session
from default.exceptions import Preenchimento_Obrigatorio, Duplicidade_Registro, Preenchimento_Invalido
from modulos.seguranca.models import ADMINISTRADOR, PERFIL
from modulos.seguranca.models.model import Usuario

# contantes de acao
INCLUSAO = 1
ALTERACAO = 2


class SegurancaController:
    def salvar(self, object):
        try:
            session.add(object)
            session.commit()
        except Exception as error:
            session.rollback()
            raise

    def addUsuario(self, pLogin='', pSenha='', pEmail='', pPerfil=0, pUsuarioLog=0):
        """


        :param pPerfil: inteiro ou CONSTANTE contendo o perfil do usuario
        :param pLogin: string de login
        :param pSenha: string de senha
        :param pEmail: string de email
        :param pUsuarioLog: inteiro com o id do usuario que está fazendo a operacao
        """
        usuario = Usuario()
        usuario.usuario_log = pUsuarioLog
        usuario.login = pLogin.strip()
        usuario.senha = generate_password_hash(pSenha.strip())
        usuario.email = pEmail.strip()
        usuario.perfil = pPerfil

        self.__validaUsuario(usuario, INCLUSAO)

        self.salvar(usuario)

    def __validaUsuario(self, usuarioObject, pAcao):

        #validando campos de preenchimento obrigatório
        if usuarioObject.login == '' or usuarioObject.login == None:
            raise Preenchimento_Obrigatorio('login')
        if usuarioObject.senha == '':
            raise Preenchimento_Obrigatorio('senha')
        if usuarioObject.email == '':
            raise Preenchimento_Obrigatorio('email')

        #validando registros duplicados
        if pAcao == INCLUSAO:
            if usuarioObject in session.query(Usuario).filter_by(login=usuarioObject.login):
                raise Duplicidade_Registro('login')
        if pAcao == ALTERACAO:
            if session.query(Usuario).filter_by(login=usuarioObject.login).count() >= 2:
                raise Duplicidade_Registro('login')

        #validando campos com preenchimento inválido
        if usuarioObject.perfil not in PERFIL.keys():
            raise Preenchimento_Invalido(u'perfil de usuário')


    def configuraUsuarioAdministrador(self):
        # só realiza a criacao do usuario administrador se a tabela estiver vazia
        if not session.query(Usuario).all():
            login = raw_input('Informe o login para o Administrador: ')
            senha = raw_input('Informe a senha para o Administrador: ')
            email = raw_input('Informe um email para o Administrador: ')

            usuario = Usuario()
            usuario.usuario_log = -1
            usuario.login = login.strip()
            usuario.senha = generate_password_hash(senha.strip())
            usuario.email = email.strip()
            usuario.perfil = ADMINISTRADOR

            self.salvar(usuario)


if __name__ == '__main__':
    # print session.query(Usuario).filter_by(login='jotage.sales').all()
    try:
        SegurancaController().addUsuario('jotage.sales212', '123', 'fsdfs', 10, -1)
    except Exception as error:
        print error.message
