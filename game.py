import numpy
import tetris

class player():

	def __init__(self):
		self.score = 0
		self.trion = tetris.tetrion()
		self.ID = None
		self.level = None
		self.highscore = None

	def update(self, opponent_event):
		# update player specific game state based on
		# opponents event and previous game state
		pass

	def get_button_presses(self):
		pass

class game():

	def __init__(self):
		self.update_time = 140 # ms
		self.p1 = player()
		# self.p2 = player()

	def update(self):
		# slow clock: update player 1 and player 2 game states
		# handles communication between game states
		# fast clock: update current tetromino orientation
		# based on user input
		pass
