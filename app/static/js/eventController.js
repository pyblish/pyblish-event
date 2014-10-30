"use strict";
/*global angular*/
/*global events*/


(function () {

    var app = angular.module("pyblishApp");

    app.controller("EventController", function (EventService) {
        this.sections = ["instance", "comment", "author", "date"];
        this.events = EventService.events;
        this.EventService = EventService;
    });

}());