var socket = io.connect('http://'
                        + document.domain
                        + ':' + location.port
                        + "/test");

socket.on('connect', function() {
	console.log("Connected!");
});

socket.on('event', function(message) {
	$("div#events").prepend("<div><a href=\"/event/" + message.name + "\">" + message.name + "</a></div>");
});