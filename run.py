from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
import game
import numpy

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app)
thread = None
thread_lock = Lock()

# create game
pptetris = None

@app.route('/')
def index():
	# initialize game
	pptetris = game.game()
	# store client ID hash
	return pptetris.p1.trion.playfield.tolist()
	return render_template('index.html', async_mode=socketio.async_mode)

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1

@socketio.on('connect', namespace='/tetris')
def connect():
	global thread
	with thread_lock:
		if thread is None:
			thread = socketio.start_background_task(target=background_thread)
			emit('connection_successful', {'data': 'Now connected to tetris backend.'})


@socketio.on('connection_callback', namespace='/tetris')
def connection_callback(message):
	print message['data']

@socketio.on('keypress', namespace='/tetris')
def keypress(data):
	if data['key'] is "ArrowRight":
		pptetris.p1.trion.move_right()
		return pptetris.p1.trion.playfield.tolist()
	elif data['key'] is "ArrowLeft":
		pptetris.p1.trion.move_left()
		return pptetris.p1.trion.playfield.tolist()
	elif data['key'] is "ArrowUp":
		pptetris.p1.trion.rot()
		return pptetris.p1.trion.playfield.tolist()

@app.route('/iterate') # Needs to emit to all clients on a thread per second
def iterate():
	pptetris.iterate()
	if pptetris.p1.trion.game_over:
		return 0
	return pptetris.p1.trion.playfield.tolist()

if __name__ == '__main__':
	if 'debug' in sys.argv:
		print('Running app in DEBUG mode.')
		socketio.run(app, debug=True)
	else:
		socketio.run(app)

