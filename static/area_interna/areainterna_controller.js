//usando jquery junto com o angularJs
	$(document).ready(function() {
                  $('#btnNovo').click(function(){
                        $('#modalFormCadUsuario').modal('show')
						$("#txtLogin").focus()
                  })
				  				  
            })

/* 
*  CONTROLLER PARA USUÁRIOS
*/
app.controller('usuarioCtrl', function($scope, $http){
	
	$scope.salvarUsuario = function(usuario) {
		$http.post('/areainterna/cadastroUsuario', usuario)
			.success(function(data) {
				$scope.usuarios.push(data.item)
				delete($scope.user)
				$("#txtLogin").focus()
			})
			.error(function(data) {
				alert(data.msg)
			})
	}
	
	$scope.editarUsuario = function(usuario){
		$scope.user = usuario		
		$('#modalFormCadUsuario').modal('show')
	}	
	
	$scope.excluirUsuario = function(usuario){
		var url = '/areainterna/excluirUsuario/' + usuario.id
		$http.delete(url)
			.success(function(){
				//TODO: verificar como remover um regisro de um array em javascript
				delete(usuario)
				alert('Usuário excluido com sucesso!')
				window.location = '/areainterna/cadastroUsuario'
			})
			.error(function(data) {
				console.log(data)
				alert('Ocorreu um erro ao tentar excluir o usuário, por gentileza consulte os logs para mais detalhes.')
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
	
	$scope.listaExcluisao = []
	$scope.atualizaListaExclusao = function (idUsuario) {
		$scope.listaExcluisao.push(idUsuario)
	}
	
	//fazendo as chamadas ao carregar a página
	var init = function() {
		$scope.consultaPerfil()
		$scope.consultaUsuarios()
	}()
})


/*
*  controller para produtos
*/
app.controller('produtoCtrl', function($scope, $http) {
	//usando jquery junto com o angularJs
	$(document).ready(function() {
                  $('#btnNovo').click(function(){
                        $('#modalFormCadProduto').modal('show')
                  })
            })	
})