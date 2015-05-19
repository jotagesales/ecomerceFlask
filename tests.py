from modulos.seguranca.controller.controller import SegurancaController, session
from modulos.seguranca.models.model import Usuario
from modulos.seguranca.models import PERFIL
from modulos.pedidos.models.model import Produto

from default.engine import session


print SegurancaController().consultaUsuario(1)