"use strict";
/*global angular*/


(function () {

    var app = angular.module("pyblishApp");

    app.controller("EventController", function (eventModel, socketIo) {

        this.sections = ["instance", "comment", "author", "date"];
        this.model = eventModel;

        // Emitted by Flask upon first connect.
        socketIo.on("connected", function (host) {
            console.log("Connected to " + host);
        });

        // Emitted upon first connect, and carries relevant initial data
        socketIo.on("init", function (data) {
            eventModel.initEvents(data);
        });

        // Emitted upon receiving a new event
        socketIo.on("event", function (event) {
            eventModel.addEvent(event);
        });

    });
}());