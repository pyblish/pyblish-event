"use strict";
/*global angular*/

(function () {

    var app = angular.module("pyblishApp", ["ngRoute"]);

    app.config(function ($routeProvider, $locationProvider) {
        $routeProvider
            .when("/", {
                templateUrl: "static/views/home.html"
            })
            .otherwise("/");

        $locationProvider.html5Mode(true);
    });

}());