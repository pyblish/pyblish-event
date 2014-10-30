"use strict";
/*global angular*/


(function () {

    var app = angular.module("pyblishApp");

    app.directive("filterList", function () {
        return {
            restrict: "E",
            controller: "FilterController",
            controllerAs: "filterCtrl",
            templateUrl: "static/templates/filter-list.html"
        };
    });

}());