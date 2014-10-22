"use strict";
/*global angular*/

angular.module("EventApp")
    .filter("reverse", function () {
        return function (items) {
            return items.slice().reverse();
        };
    });