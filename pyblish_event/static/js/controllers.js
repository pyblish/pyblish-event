"use strict";
/*global angular*/


/** Display each event in a list
*
* @param {Service} searchModel - Used for communicating between
*       Navigation and list
*/
function ListCtrl(searchModel, socket) {
    // this.model.events = [];

    socket.on("connected", function (data) {
        // Initialise with data from server
        console.log("Someone connected: " + data.whois);
        console.log("And set events: " + data.events);
        searchModel.events = data.events;
    });

    this.model = searchModel;
}


/**
* Handle navigation and search
*
*/
function NavCtrl(searchModel, socket) {
    this.model = searchModel;
    this.socket = socket;
}


NavCtrl.prototype.search = function (query) {
    this.model.updateQuery(query);
    this.socket.emit(query);
};



angular.module("EventApp")
    .controller("ListCtrl", ListCtrl)
    .controller("NavCtrl", NavCtrl);
