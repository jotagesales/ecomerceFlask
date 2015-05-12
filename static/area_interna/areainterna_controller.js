
app.controller('usuarioCtrl', function($scope, $http){
	
	$scope.addUsuario = function(usuario){
		
	}
	
	$scope.salvar = function(usuario) {
		$http.post('/areainterna/cadastroUsuario', usuario)
			.success(function(data) {
				alert(data.msg)
			})
			.error(function(data) {
				alert(data.msg)
			})
	}
	
	
	$scope.excluir = function(usario){
		console.log('clicou')
	}
	
	
	$scope.consultaUsuarios = function(params) {
		$http.get('/areainterna/consultaUsuarios')
			.success(function(data){
				$scope.usuarios = data.items
			})
			.error(function(data){
				console.log(data)
			})
	}
	
	$scope.consultaPerfil = function() {
		$http.get('/areainterna/consultaPerfil')
			.success(function(data) {
				$scope.perfis = data.items
			})
			.error(function(data) {
				alert('Ocorreu um erro ao tentar consultar os perfis de usuário')
			})
	}
	
	$scope.validaUsuario = function(usuario) {
		if (usuario == undefined){
			return true
		}
		return (!usuario.login || !usuario.email || !usuario.perfil || !usuario.senha)
	}
	
	//fazendo as chamadas ao carregar a página
	var init = function() {
		$scope.consultaPerfil()
		$scope.consultaUsuarios()
	}()
})