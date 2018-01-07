import numpy as np

# http://tetris.wikia.com/wiki/Gameplay_overview

class tetromino():

	def __init__(self, color, structure):
		self.structure = structure # np array
		x = np.random.randint(10 - shape(self.structure)[1])
		self.loc = np.array([0, x]) # top left corner in playfield
		self.color = color 		

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

class tetrion():

	def __init__(self, curr_mino, next_mino):
		self.h = 20 # standard size, use global var?
		self.w = 10 # this is also used in tetromino class
		self.curr_mino = curr_mino
		self.curr_mino_field = np.zeros((self.h, self.w))
		self.save_mino = None
		self.playfield = np.zeros((self.h, self.w))
		# playfield should not contain current tetromino -
		# build a blank playfield with tetrmonio and
		# do a matrix addition to include it

	def move_right(self):
		if self.curr_mino.get_bboxE() + 1 < self.w:		
			self.curr_mino.move_right()
		if self.mino_collides():
			self.curr_mino.move_left()
		# refresh mino_field

	def move_left(self):
		if self.curr_mino.get_bboxW() - 1 >= 0:
			self.curr_mino.move_left()
		if self.mino_collides():
			self.curr_mino.move_right()
		# refresh mino_field

	def mino_collides(self):
		return (self.curr_mino_field > 1).any() # use logical indexing?

	def add_row_to_bot(self):
		pass

	def update(self):
		pass





