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

'use strict';

angular.module('tetrisApp')
  .controller('boardController', ['$scope', 'socket', function($scope, socket) {

    socket.on('connect', function() { 
    	socket.emit('connection_callback', {data: 'connected!'});
    });

    socket.on('connection_successful', function(msg) {
    	console.log(msg.data);
    });

    socket.on('update_board', function(data) {
		$scope.$applyAsync(function(){
			$scope.board = data.board;
		});
    });

    socket.on("keypress", function(key) {
    	socket.emit('connection_callback', {data: 'connected!'});
    	console.log(key);
    });
}]);