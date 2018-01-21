import numpy as np

# http://tetris.wikia.com/wiki/Gameplay_overview

class tetromino():

	def __init__(self, color, structure):
		self.structure = structure # np array
		self.color = color
		x = np.random.randint(10 - np.shape(self.structure)[1])
		self.loc = np.array([0, x]) # top left corner in playfield	

	def move_up(self):
		self.loc[0] -= 1

	def move_down_by(self, delta):
		assert(delta > 0)
		self.loc[0] += delta

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
		x = np.random.randint(10 - np.shape(self.structure)[1])
		self.loc = np.array([0, x]) # top left corner in playfield
		self.structure = np.rot90(self.structure, np.random.randint(4))

class tetrion():

	def __init__(self):
		self.height = 20 # standard size, use global var?
		self.width = 10 # this is also used in tetromino class
		self.unique_minos = self.define_tetrominoes()
		self.curr_mino = self.create_new_mino()
		self.save_mino = None
		self.playfield = np.zeros((self.height, self.width))
		self.game_over = False
		# playfield should not contain current tetromino -
		# build a blank playfield with tetrmonio and
		# do a matrix addition to include it

	def move_right(self):
		if self.curr_mino.get_bboxE() + 1 < self.width:		
			self.curr_mino.move_right()
		if self.mino_collides():
			self.curr_mino.move_left()

	def move_left(self):
		if self.curr_mino.get_bboxW() - 1 >= 0:
			self.curr_mino.move_left()
		if self.mino_collides():
			self.curr_mino.move_right()

	def move_down(self):
		if self.curr_mino.get_bboxS() + 1 < self.height:
			self.curr_mino.move_down_by(1)
		if self.mino_collides():
			self.curr_mino.move_up()

	def drop(self):
		x0 = self.curr_mino.get_bboxW
		x1 = self.curr_mino.get_bboxE
		curr_cols = self.playfield[:,x0:(x1+1)]
		row_has_block = [(row>0).any() for row in curr_cols]
		first_block_y = argmax(row_has_block)
		delta = first_block_y - self.curr_mino.get_bboxS - 1
		self.curr_mino.move_down_by(delta)

	def rot(self):
		self.curr_mino.rotcw()
		if self.curr_mino.get_bboxE() >= self.width or self.mino_collides():
			self.curr_mino.rotccw()
		sze = np.shape(self.curr_mino.structure)
		if sze[0] == 1:
			self.move_left()
		if sze[1] == 1:
			self.move_right()

	def mino_collides(self):
		x0 = self.curr_mino.get_bboxW()
		x1 = self.curr_mino.get_bboxE()+1
		y0 = self.curr_mino.get_bboxN()
		y1 = self.curr_mino.get_bboxS()+1
		position_to_test = self.playfield[y0:y1,x0:x1] > 0
		curr_position = self.curr_mino.structure > 0
		return (position_to_test & curr_position).any()

	def add_mino_to_field(self):
		self.playfield = self.get_game_board()
		self.create_new_mino()

	def get_game_board(self):
		display_board = np.zeros(np.shape(self.playfield))
		x0 = self.curr_mino.get_bboxW()
		x1 = self.curr_mino.get_bboxE()+1
		y0 = self.curr_mino.get_bboxN()
		y1 = self.curr_mino.get_bboxS()+1
		display_board[y0:y1,x0:x1] = self.curr_mino.color * self.curr_mino.structure
		display_board = display_board + self.playfield
		return display_board

	def create_new_mino(self):
		rand_mino_idx = np.random.randint(len(self.unique_minos))
		self.curr_mino = self.unique_minos[rand_mino_idx]
		new_mino = tetromino(self.curr_mino.color, self.curr_mino.structure)
		self.unique_minos[rand_mino_idx] = new_mino

	def add_row_to_bot(self):
		# push up the current tetromino if collision occurs
		pass

	def iterate(self):

		# debug
		print ""
		print "iterate"
		print ""
		# debug

		if self.curr_mino.get_bboxS()+1 == self.height:
			self.add_mino_to_field()
			return
		self.curr_mino.move_down_by(1)
		if self.mino_collides():
			self.curr_mino.move_up()
			if self.curr_mino.get_bboxN() == 0:
				self.game_over = True
				return
			self.add_mino_to_field()
			return
		row_filled = [(row>0).all() for row in self.playfield]
		if any(row_filled):
			unfilled_rows = self.playfield[not row_filled]
			new_playfield = np.zeros(np.shape(self.playfield))
			new_playfield[(self.height-np.shape(unfilled_rows)[0]):] = unfilled_rows


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
			minos.append( tetromino(i+1, structures[i]) )
		return minos


