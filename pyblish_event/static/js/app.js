"use strict";
/*global angular*/


angular.module("EventApp", ["ngRoute", "ui.bootstrap"])
    .config(function ($routeProvider, $locationProvider) {
        // Provide an overview of contacts available in our application
        $routeProvider
            .when("/events", {
                controller: "ListCtrl",
                controllerAs: "list",
                templateUrl: "static/views/list.html"
            })
            .otherwise("/events");

        // Remove the # from urls, as HTML5 is capable of dynamically
        // switching URLs and thus won"t need the hash-bang.
        $locationProvider.html5Mode(true);
    });