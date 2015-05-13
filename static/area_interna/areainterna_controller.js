
app.controller('usuarioCtrl', function($scope, $http){
	
	$scope.addUsuario = function(usuario){
		
	}
	
	$scope.salvar = function(usuario) {
		$http.post('/areainterna/cadastroUsuario', usuario)
			.success(function(data) {
				$scope.usuarios.push(data.item)
				delete(usuario)
			})
			.error(function(data) {
				alert(data.msg)
			})
	}
	
	$scope.editar = function(usuario){
		$scope.usuario = usuario
	}	
	
	$scope.excluir = function(usuario){
		var url = '/areainterna/excluirUsuario/' + usuario.id
		$http.delete(url)
			.success(function(){
				//TODO: verificar como remover um regisro de um array em javascript
				delete(usuario)
			})
			.error(function() {
				alert('deu ruim :(')
			})
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