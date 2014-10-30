"use strict";
/*global angular*/


(function () {
    var app = angular.module("pyblishApp");

    app.controller("FilterController", function (EventService) {
        this.key = "";
        this.EventService = EventService;
    });

}());