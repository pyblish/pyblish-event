"use strict";
/*global angular*/


(function () {
    var app = angular.module("pyblishApp");

    app.controller("FilterController", function (eventService) {
        this.key = "";
        this.eventService = eventService;
    });

}());