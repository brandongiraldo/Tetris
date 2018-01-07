from flask import Flask, render_template
from flask_socketio import SocketIO
import sys
import game
import numpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app)

# create game
pptetris = None

@app.route('/')
def index():
	# initialize game
	pptetris = game.game()
	# store client ID hash
	return pptetris.p1.trion.playfield.tolist()

@app.route('/right') # Fix to sockets
def right():
	pptetris.p1.trion.move_right()
	return pptetris.p1.trion.playfield.tolist()

@app.route('/left') # Fix to sockets
def left():
	pptetris.p1.trion.move_left()
	return pptetris.p1.trion.playfield.tolist()

@app.route('/rot') # Fix to sockets
def rot():
	pptetris.p1.trion.rot()
	return pptetris.p1.trion.playfield.tolist()

@app.route('/iterate') # Fix to sockets
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

