"use strict";
/*global angular*/
/*global events*/
/*global io*/


(function () {

    var app = angular.module("pyblishApp", ["ngRoute",
                                            "ui.utils",
                                            "ui.bootstrap",
                                            "btford.socket-io"]);

    // Socket.io support, from btford.socket-io
    app.factory('socketIo', function (socketFactory) {
        return socketFactory({
            ioSocket: io.connect("/default")
        });
    });

    // Routing
    app.config(function ($routeProvider, $locationProvider) {
        $routeProvider
            .when("/", {
                templateUrl: "static/views/home.html",
            })
            .otherwise("/");

        // Do not display hash-tag in URL
        $locationProvider.html5Mode(true);
    });

}());