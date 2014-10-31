"use strict";
/*global angular*/


(function () {
    var app = angular.module("pyblishApp");

    app.controller("NavigationController", function (eventService) {
        this.eventService = eventService;
    });

}());