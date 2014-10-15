var PackLlama = angular.module("PackLlama", ["ngRoute", "ngCookies", function($interpolateProvider){
    $interpolateProvider.startSymbol("{[{");
    $interpolateProvider.endSymbol("}]}");
    );

PackLlama.run(function ($http, $cookies){
    $http.default.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

PackLlama.config(function($routerProvider){
    $routerProvider
        .when("/", {
            templateUrl: "dashboar",
        })
        .oderwise({
            redirectTo: '/'
        });
