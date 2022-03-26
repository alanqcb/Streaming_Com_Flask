var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope,$http) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";

    $scope.lista = ['nome','idade','endereco']
    $scope.lista_catalogo = [];



    $http({
        method: 'GET',
        url: '/streaming_mod/read?update=yes'
      }).then(function successCallback(response) {
          console.log(response.data)
          $scope.lista_catalogo = response.data;
          // this callback will be called asynchronously
          // when the response is available
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
        });



});