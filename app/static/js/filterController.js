"use strict";
/*global angular*/


(function () {
    var app = angular.module("pyblishApp");

    app.controller("FilterController", function (eventModel) {
        this.key = "";
        this.model = eventModel;
    });

}());