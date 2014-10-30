"use strict";
/*global angular*/


(function () {

    var app = angular.module("pyblishApp");

    app.directive("eventList", function () {
        return {
            restrict: "E",
            controller: "EventController",
            controllerAs: "eventCtrl",
            templateUrl: "static/templates/event-list.html"
        };
    });

}());