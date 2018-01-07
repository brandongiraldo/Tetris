import numpy as np

# http://tetris.wikia.com/wiki/Gameplay_overview

class tetromino():

	def __init__(self, color, structure):
		self.structure = structure # np array
		self.color = color
		x = np.random.randint(10 - shape(self.structure)[1])
		self.loc = np.array([0, x]) # top left corner in playfield	

	def move_right(self):
		self.loc[1] += 1

	def move_left(self):
		self.loc[1] -= 1

	def rotcw(self):
		self.structure = np.rot90(self.structure, 3)

	def rotccw(self):
		self.structure = np.rot90(self.structure)

	def get_bboxN(self):
		return self.loc[0]

	def get_bboxE(self):
		return self.loc[1] + np.shape(self.structure)[1] - 1

	def get_bboxS(self):
		return self.loc[0] + np.shape(self.structure)[0] - 1

	def get_bboxW(self):
		return self.loc[1]

	def reset(self):
		x = np.random.randint(10 - shape(self.structure)[1])
		self.loc = np.array([0, x]) # top left corner in playfield
		self.structure = np.rot90(self.structure, np.random.randint(4))

class tetrion():

	def __init__(self, curr_mino, next_mino):
		self.h = 20 # standard size, use global var?
		self.w = 10 # this is also used in tetromino class
		self.curr_mino = curr_mino
		self.save_mino = None
		self.playfield = np.zeros((self.h, self.w), dtype=bool)
		self.unique_minos = self.define_tetrominoes()
		# playfield should not contain current tetromino -
		# build a blank playfield with tetrmonio and
		# do a matrix addition to include it

	def move_right(self):
		if self.curr_mino.get_bboxE() + 1 < self.w:		
			self.curr_mino.move_right()
		if self.mino_collides():
			self.curr_mino.move_left()

	def move_left(self):
		if self.curr_mino.get_bboxW() - 1 >= 0:
			self.curr_mino.move_left()
		if self.mino_collides():
			self.curr_mino.move_right()

	def rotccw(self):
		self.curr_mino.rotccw()
		if self.mino_collides():
			self.curr_mino.rotcw()

	def rotcw(self):
		self.curr_mino.rotcw()
		if self.mino_collides():
			self.curr_mino.rotccw()

	def mino_collides(self):
		x0 = self.curr_mino.get_bboxW
		x1 = self.curr_mino.get_bboxE
		y0 = self.curr_mino.get_bboxN
		y1 = self.curr_mino.get_bboxS
		position_to_test = self.curr_mino_field[y0:y1,x0:x1]
		return (position_to_test & curr_mino.structure).any()

	def add_mino_to_field(self):
		x0 = self.curr_mino.get_bboxW
		x1 = self.curr_mino.get_bboxE
		y0 = self.curr_mino.get_bboxN
		y1 = self.curr_mino.get_bboxS
		self.curr_mino_field[y0:y1,x0:x1] = self.curr_mino.structure

	def create_new_mino(self):
		idx = numpy.random.randint(length(unique_minos))
		self.curr_mino = unique_minos[idx]
		unique_minos[idx] = tetromino(self.curr_mino.color, self.curr_mino.structure)

	def add_row_to_bot(self):
		pass

	def update(self):
		pass

	def define_tetrominoes(self):
		# populate self.minos
		structures = []
		structures.append(np.array([	[1, 1, 1, 1]	]),		dtype=bool)
		structures.append(np.array([	[1, 0, 0]		,\
										[1, 1, 1]		]),		dtype=bool)
		structures.append(np.array([	[0, 0, 1]		,\
										[1, 1, 1]		]),		dtype=bool)
		structures.append(np.array([	[1, 1]			,\
										[1, 1]			]),		dtype=bool)
		structures.append(np.array([	[0, 1, 1]		,\
										[1, 1, 0]		]),		dtype=bool)
		structures.append(np.array([	[0, 1, 0]		,\
										[1, 1, 1]		]),		dtype=bool)
		structures.append(np.array([	[1, 1, 0]		,\
										[0, 1, 1]		]),		dtype=bool)
		minos = []
		for i in range(len(structures)):
			minos.append( tetromino(i, structures[i]) )
		return minos






