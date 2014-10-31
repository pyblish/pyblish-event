// Central data source for events and event-processing

"use strict";
/*global angular*/


(function () {

    var app = angular.module("pyblishApp");


    /**
    * Shared model across Main Body and Navigation
    * for search queries.
    */
    function EventModel() {
        return {
            selectedFilters: [],
            maxResults: 30,
            events: [],
            key: "",

            initEvents: function (events) {
                /**
                * Initialise events from server
                */
                this.events = events;
            },

            addEvent: function (event) {
                /**
                * Add an event
                */
                this.events.push(event);
            },
        };
    }


    app.factory("eventModel", EventModel);

}());
