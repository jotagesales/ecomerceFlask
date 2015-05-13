# -*- coding: utf-8 -*-
from functools import wraps

from flask import session, redirect, url_for

def login_required(func):
	"""
	O decorator login_required verifica se o usuário está logado,
	para isso é necessário ter o id do usuário logado na seção, caso
	não tenha ele redireciona para fazer login.
	"""
	@wraps(func)
	def decorator(*args, **kwargs):
		if not session.get('id_usuario_logado'):
			return redirect(url_for('areainterna.login'))
		return func(*args, **kwargs)
	
	return decorator
	