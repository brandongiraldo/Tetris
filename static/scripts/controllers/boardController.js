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
    console.log("loaded controller");
    socket.on('connect', function() { 
    	socket.emit('connection_callback', {data: 'connected!'});
    });

    socket.on('connection_successful', function(msg) {
    	console.log(msg.data);
    });

    socket.on('update_board', function(data) {
    	data.board.forEach(function(row){
    		console.log(row);
    	});
		$scope.$applyAsync(function(){
			$scope.board = data.board;
		});
    	// $scope.test = "test";
    	// console.log($scope.test);
    	// $scope.board = data.board;
    	// console.log(data.board);
    });

    socket.on("keypress", function(key) {
    	socket.emit('connection_callback', {data: 'connected!'});
    	console.log(key);
    });
}]);