var app = angular.module('app_pedidos', [])
			
			app.config(['$interpolateProvider', function($interpolateProvider) {
				$interpolateProvider.startSymbol('[[');
				$interpolateProvider.endSymbol(']]');
			}]);