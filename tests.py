from modulos.seguranca.controller.controller import SegurancaController
from modulos.seguranca.models import PERFIL

print PERFIL

lista =[]
for i in PERFIL.keys():
	lista.append({'codigo':i, 'descricao': PERFIL[i]})
	
print lista 