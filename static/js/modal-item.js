var app = angular.module("appSunDos", ['ngCookies']);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.config(['$httpProvider',
    function(provider) {
        provider.defaults.xsrfCookieName = 'csrftoken';
        provider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);

app.controller('ItemsController', function($scope, $sce, $http) {
    $scope.veureProducte = function(item) {
        $http.post("https://sun2-riusses.c9users.io/item/", {
            id: item,
        }).success(function(dades) {
            $scope.Producte = {};
            $scope.Producte.nom = dades.resposta.nom;
            $scope.Producte.resum = dades.resposta.resum;
            $scope.Producte.video = $sce.trustAsResourceUrl(dades.resposta.video);
        });
    };
});