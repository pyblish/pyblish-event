"use strict";
/*global angular*/


(function () {

    var app = angular.module("pyblishApp");

    app.directive("navigation", function () {
        return {
            restrict: "E",
            controller: "NavigationController",
            controllerAs: "navCtrl",
            templateUrl: "static/templates/navigation.html",
        };
    });

}());