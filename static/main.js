$(document).ready(function() {
    namespace = '/tetris';
    // Connect to the Socket.IO server.
    // The connection URL has the following format:
    //     http[s]://<domain>:<port>[/<namespace>]
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    
    socket.on('connect', function() { 
    	socket.emit('connection_callback', {data: 'connected!'});
    });

    socket.on('connection_successful', function(msg) {
    	console.log(msg.data);
    	console.log($('#connected'));
        $('#connected').append('<br>' + $('<div/>').text(msg.data).html());
    });

    socket.on('update_board', function(data) {
    	$("#board").empty();
    	data.board.forEach(function(row){
    		console.log(row);
    		var line = document.createElement("li");
    		line.innerHTML = row
    		$('#board').append(line); 
    	});
    });

    socket.on("keypress", function(key) {
    	socket.emit('connection_callback', {data: 'connected!'});
    	console.log(key)
    });

    $(document).keydown(function(e) {
    	switch (event.key) {
		    case "ArrowDown":
		    case "ArrowUp":
		    case "ArrowLeft":
		    case "ArrowRight":
		    socket.emit("keypress", {key: event.key});
		    break;
	    	default:
			return;
		}
	});
});