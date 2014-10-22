"use strict";
/*global angular*/


/**
* Shared model across Main Body and Navigation
* for search queries.
*/
function SearchModel() {
    var searchModel = {
        query: ""
    };

    searchModel.updateQuery = function (query) {
        searchModel.query = query;
    };
    return searchModel;
}

angular.module("EventApp")
    .factory("searchModel", SearchModel);