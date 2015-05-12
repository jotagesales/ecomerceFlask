from modulos.seguranca.controller.controller import SegurancaController, session
from modulos.seguranca.models.model import Usuario
from modulos.seguranca.models import PERFIL

lst= []
for i in range(10001, 10								0000):
	usuario = Usuario()
	usuario.login = 'teste performace ' + str(i)
	usuario.senha = 'secret' 
	usuario.email = 'secret' 
	usuario.perfil = 1
	usuario.usuario_log = -1
	
	lst.append(usuario)
	
session.add_all(lst)
session.commit()