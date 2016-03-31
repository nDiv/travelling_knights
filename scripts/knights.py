# Defining a Chess grid class and a Knight player class.

import random

class Game:
	
	def __init__(self):
		self.black = [0,0]
		self.white = [7,7]
		self.game_on = True

	def play(self, black, white):

		while(self.game_on):

			white.Move()
			if(not self.update(white)):
				self.game_on = False
				#print("Game over!")
				break

			black.Move()
			if(not self.update(black)):
				self.game_on = False
				#print("Game over!")
				break
		if(black.moves == white.moves):
			return black.moves
		else:
			raise TypeError("Something went wrong! Knights must finish with same number moves")
		
	def update(self, knight):
		if(knight.idx == 1):
			if(knight.x == self.white[0] and knight.y == self.white[1]):
				#print("Black knight won!")
				return False
			else:
				self.black[0] = knight.x
				self.black[1] = knight.y
				#knight.moves += 1
				return True
		elif(knight.idx == 2):
			if(knight.x == self.black[0] and knight.y == self.black[1]):
				#print("White knight won!")
				return False
			else:
				self.white[0] = knight.x
				self.white[1] = knight.y
				#knight.moves += 1
				return True
		else:
			raise TypeError("Invalid Knight! id must either be 1 or 2") 
		
	def reset(self):
		self.black = [0,0]
		self.white = [7,7]
		self.game_on = True

class Knight:
	
	def __init__(self, idx):
		self.idx = idx # must be 1 for black and 2 for white.
		self.moves = 0

		if(idx == 1):
			self.x = 0
			self.y = 0
		elif(idx == 2):
			self.x = 7
			self.y = 7
		else:
			raise TypeError("Invalid id given! id must either be 1 or 2") 

	def reset(self):

		if(self.idx == 1):
			self.x = 0
			self.y = 0
		else:
			self.x = 7
			self.y = 7

		self.moves = 0

	def Move(self):
		x = [self.x-1,self.x-2,self.x-2,self.x-1,self.x+1,self.x+2,self.x+2,self.x+1]
		y = [self.y-2,self.y-1,self.y+1,self.y+2,self.y+2,self.y+1,self.y-1,self.y-2]

		ind = []
		for i in range(len(x)):
			if(x[i] >= 0 and x[i] < 8 and y[i] >= 0 and y[i] < 8):
				ind.append(i)

		j = random.randint(0,len(ind)-1)
		self.x = x[ind[j]]
		self.y = y[ind[j]]
		self.moves += 1

