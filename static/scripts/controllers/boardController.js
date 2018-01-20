// $(document).ready(function() {

//     var socket = io.connect("http://localhost:" + location.port);

//     $(document).keydown(function(e) {
//     	switch (event.key) {
// 		    case "ArrowDown":
// 		    case "ArrowUp":
// 		    case "ArrowLeft":
// 		    case "ArrowRight":
// 		    socket.emit("keypress", {key: event.key});
// 		    break;
// 	    	default:
// 			return;
// 		}
// 	});
// });

'use strict';

angular.module('tetrisApp')
  .controller('boardController', ['$scope', 'socket', function($scope, socket) {

    console.log("made it!");

    socket.on('connect', function() { 
    	socket.emit('connection_callback', {data: 'connected!'});
    });

    socket.on('connection_successful', function(msg) {
    	console.log(msg.data);
    	console.log($('#connected'));
        $('#connected').append('<br>' + $('<div/>').text(msg.data).html());
    });

    socket.on('update_board', function(data) {
    	data.board.forEach(function(row){
    		console.log(row);
    	});
    });

    socket.on("keypress", function(key) {
    	socket.emit('connection_callback', {data: 'connected!'});
    	console.log(key)
    });
}]);