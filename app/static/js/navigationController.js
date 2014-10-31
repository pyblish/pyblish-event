"use strict";
/*global angular*/


(function () {
    var app = angular.module("pyblishApp");

    app.controller("NavigationController", function (eventModel) {
        this.model = eventModel;
    });

}());