"use strict";
/*global angular*/

(function () {

    var app = angular.module("pyblishApp");

    app.filter("reverse", function () {
        return function (items) {
            return items.slice().reverse();
        };
    });

}());