'use strict';

angular.module('tetrisApp')
  .controller('boardController', ['$scope', 'socket', function($scope, socket) {

    $scope.key = function($event) {
        console.log($event.keyCode);
        if ($event.keyCode == 38)
            console.log("up arrow");
        else if ($event.keyCode == 39)
            console.log("right arrow");
        else if ($event.keyCode == 40)
            console.log("down arrow");
        else if ($event.keyCode == 37)
            console.log("left arrow");
    }

    socket.on('connect', function() { 
    	socket.emit('connection_callback', {data: 'connected!'});
    });

    socket.on('connection_successful', function(msg) {
    	console.log(msg.data);
    });

    socket.on('update_board', function(data) {
        console.log(data);
		$scope.$applyAsync(function(){
			$scope.board = data;
		});
    });

    socket.on("keypress", function(key) {
    	socket.emit('connection_callback', {data: 'connected!'});
    	console.log(key);
    });
}]);