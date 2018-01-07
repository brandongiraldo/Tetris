import numpy
import tetris

class player():

	def __init__(self):
		self.score = 0
		self.trion = tetrion()

	def update(opponent_event):
		# update player specific game state based on
		# opponents event and previous game state
		pass


class game():

	def __init__(self):
		self.update_time = 140 # ms
		self.p1 = player()
		self.p2 = player()
		self.unique_minos = self.define_tetrominoes()

	def define_tetrominoes(self):
		# populate self.minos
		structures = []
		structures.append(np.array([	[1, 1, 1, 1]	]))
		structures.append(np.array([	[1, 0, 0]		,\
										[1, 1, 1]		]))
		structures.append(np.array([	[0, 0, 1]		,\
										[1, 1, 1]		]))
		structures.append(np.array([	[1, 1]			,\
										[1, 1]			]))
		structures.append(np.array([	[0, 1, 1]		,\
										[1, 1, 0]		]))
		structures.append(np.array([	[0, 1, 0]		,\
										[1, 1, 1]		]))
		structures.append(np.array([	[1, 1, 0]		,\
										[0, 1, 1]		]))
		minos = []
		for i in range(len(structures)):
			minos.append( tetromino(i, structures[i]) )
		return minos

	def update(self):
		# slow clock: update player 1 and player 2 game states
		# handles communication between game states
		# fast clock: update current tetromino orientation
		# based on user input
		pass
