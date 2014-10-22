"use strict";
/*global angular*/


/** Display each event in a list
*
* @param {Service} searchModel - Used for communicating between
*       Navigation and list
*/
function ListCtrl(searchModel) {
    this.model = searchModel;

    this.model.groups = [
        {
            title: "Peter01",
            content: "Peter01 was published just now"
        },
        {
            title: "Marcus04",
            content: "Marcus04 was published 6 mins ago"
        }
    ];
}


/**
* Handle navigation and search
*
*/
function NavCtrl(searchModel) {
    this.model = searchModel;
}


NavCtrl.prototype.search = function (query) {
    this.model.updateQuery(query);
};



angular.module("EventApp")
    .controller("ListCtrl", ListCtrl)
    .controller("NavCtrl", NavCtrl);
