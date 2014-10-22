"use strict";
/*global angular*/
/*global io*/


/**
* Shared model across Main Body and Navigation
* for search queries.
*/
function SearchModel() {
    var searchModel = {
        query: "",
        events: []
    };

    searchModel.updateQuery = function (query) {
        searchModel.query = query;
    };

    return searchModel;
}


function Socket($rootScope) {
    var socket = io.connect("/event");
    return {
        on: function (eventName, callback) {
            socket.on(eventName, function () {
                var args = arguments;
                $rootScope.$apply(function () {
                    callback.apply(socket, args);
                });
            });
        },
        emit: function (eventName, data, callback) {
            socket.emit(eventName, data, function () {
                var args = arguments;
                $rootScope.$apply(function () {
                    if (callback) {
                        callback.apply(socket, args);
                    }
                });
            });
        }
    };
}


angular.module("EventApp")
    .factory("socket", Socket)
    .factory("searchModel", SearchModel);