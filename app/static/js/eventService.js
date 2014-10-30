// Central data source for events and event-processing

"use strict";
/*global angular*/
/*global events*/


(function () {

    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    // Temporary
    var events = [];
    for (var i = 50; i >= 0; i--) {
        events.push({
                instance: [
                    "Peter01",
                    "Marus02",
                    "RobotVillain05",
                    "TestBot10"
                ][getRandomInt(0, 3)],
                color: getRandomInt(0, 4),
                comment: "Some long comment here",
                author: "marcus",
                date: Date.now(),
                family: [
                    "napoleon.animation.rig",
                    "napoleon.asset.rig",
                    "napoleon.animation.cache",
                    "napoleon.asset.model",
                    "napoleon.asset.texture",
                    "napoleon.asset.shd",
                    "napoleon.asset.shader",
                    "napoleon.asset.panzar",
                    "napoleon.asset.moosh",
                    "napoleon.animation.blood",
                    "napoleon.asset.mod",
                    "napoleon.asset.abc",
                    "napoleon.asset.dawn",
                    "napoleon.asset.texture",
                ][getRandomInt(0, 13)]
            })
    };

    var app = angular.module("pyblishApp");


    /**
    * Shared model across Main Body and Navigation
    * for search queries.
    */
    function EventService() {
        return {
            key: "", // Shared key, modified by top-level navigation
            selectedFilters: [],  // Currently selected filters in the sidebar
            events: events,
        };
    }


    app.factory("EventService", EventService);

}());
