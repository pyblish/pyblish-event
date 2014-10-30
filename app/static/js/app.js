"use strict";
/*global angular*/
/*global events*/

(function () {

    var app = angular.module("pyblishApp", ["ngRoute", "ui.utils"]);

    app.config(function ($routeProvider, $locationProvider) {
        $routeProvider
            .when("/", {
                templateUrl: "static/views/home.html",
            })
            .otherwise("/");

        // Do not display hash-tag in URL
        $locationProvider.html5Mode(true);
    });

}());