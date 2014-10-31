"use strict";
/*global angular*/
/*global events*/


(function () {

    var app = angular.module("pyblishApp");

    app.controller("EventController", function (eventService, socketIo) {

        // Emitted by Flask upon first connect.
        socketIo.on("connected", function (data) {
            console.log("Connected to " + data);
        });

        this.sections = ["instance", "comment", "author", "date"];
        this.events = eventService.events;
        this.eventService = eventService;
    });

}());