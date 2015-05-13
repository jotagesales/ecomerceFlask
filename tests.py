from modulos.seguranca.controller.controller import SegurancaController, session
from modulos.seguranca.models.model import Usuario
from modulos.seguranca.models import PERFIL

lst = []
for i in range(5000):
	usuario = Usuario()
	usuario.login = 'Teste de performace ' + str(i)
	usuario.email = 'teste@performace.com.br'
	usuario.senha = 'secret'
	usuario.perfil = 1
	usuario.usuario_log = -1
	
	lst.append(usuario)

session.add_all(lst)
session.commit()