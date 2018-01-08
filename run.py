#!/usr/bin/env python

from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
import game
import numpy

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app, async_mode=async_mode)

update_board_thread = None
thread_lock = Lock()

# create game
pptetris = game.game()

@app.route('/')
def index():
	return render_template('index.html', board=pptetris.p1.trion.get_game_board().tolist(), async_mode=socketio.async_mode)

def thread_update_board():
    while True:
        socketio.sleep(1)
        pptetris.p1.trion.iterate()
        # render_template('index.html', board=pptetris.p1.trion.get_game_board().tolist())
        print pptetris.p1.trion.get_game_board()
        if pptetris.p1.trion.game_over:
        	return 0
		socketio.emit('update_board', {'board': pptetris.p1.trion.get_game_board().tolist()})

        
@socketio.on('connect')
def connect():
	global update_board_thread
	with thread_lock:
		if update_board_thread is None:
			update_board_thread = socketio.start_background_task(thread_update_board)
	emit('connection_successful', {'data': 'Now connected to tetris backend.'})
			


@socketio.on('connection_callback')
def connection_callback(message):
	print message['data']

@socketio.on('keypress')
def keypress(data):
	if data['key'] == "ArrowRight":
		pptetris.p1.trion.move_right()
	elif data['key'] == "ArrowLeft":
		pptetris.p1.trion.move_left()
	elif data['key'] == "ArrowUp":
		pptetris.p1.trion.rot()

	render_template('index.html', board=pptetris.p1.trion.get_game_board().tolist())
	emit('update_board', {'board': pptetris.p1.trion.get_game_board().tolist()})
	

if __name__ == '__main__':
	if 'debug' in sys.argv:
		print('Running app in DEBUG mode.')
		socketio.run(app, debug=True)
	else:
		socketio.run(app)

