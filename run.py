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

update_board_thread = None
thread_lock = Lock()

# create game
pptetris = game.game()

@app.route('/')
def index():
	# initialize game
	
	# global pptetris
	# pptetris = game.game()

	# store client ID hash

	print "\n"
	for row in pptetris.p1.trion.get_game_board().tolist():
		print row
	print "\n"

	return render_template('index.html', board=pptetris.p1.trion.get_game_board().tolist(), async_mode=socketio.async_mode)

def thread_update_board():
    while True:
        socketio.sleep(0.5)
        pptetris.p1.trion.iterate()
        # render_template('index.html', board=pptetris.p1.trion.get_game_board().tolist())

        print pptetris.p1.trion.get_game_board()

        if pptetris.p1.trion.game_over:
        	return 0
		emit('update_board', {'board': pptetris.p1.trion.get_game_board().tolist()})

        
@socketio.on('connect', namespace='/tetris')
def connect():
	global update_board_thread
	with thread_lock:
		if update_board_thread is None:
			emit('connection_successful', {'data': 'Now connected to tetris backend.'})
			update_board_thread = socketio.start_background_task(thread_update_board)


@socketio.on('connection_callback', namespace='/tetris')
def connection_callback(message):
	print message['data']

@socketio.on('keypress', namespace='/tetris')
def keypress(data):
	if data['key'] == "ArrowRight":
		pptetris.p1.trion.move_right()
	elif data['key'] == "ArrowLeft":
		pptetris.p1.trion.move_left()
	elif data['key'] == "ArrowUp":
		pptetris.p1.trion.rot()

	emit('update_board', {'board': pptetris.p1.trion.get_game_board().tolist()})
	

if __name__ == '__main__':
	if 'debug' in sys.argv:
		print('Running app in DEBUG mode.')
		socketio.run(app, debug=True)
	else:
		socketio.run(app)

