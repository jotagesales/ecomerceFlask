
app.controller('loginCtrl', function ($scope, $http) {
	
	$scope.login = function(usuario) {
		var url = '/areainterna/login'
		$http.post(url, usuario)
			.success(function () {
				window.location = '/areainterna'
			})
			.error(function(data) {
				alert(data.mensagem)
			})
	}
})