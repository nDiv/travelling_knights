# Main file of Travelling Knights

from knights import Game, Knight
import time
import random

random.seed()
game = Game()
black = Knight(1)
white = Knight(2)

print("Game initial state: ")
print("Black night position: (%d,%d)" % (game.black[0],game.black[1]))
print("Black night position: (%d,%d)" % (game.white[0],game.white[1]))

trials = 10**9
moves = 6
prob = 0
startT = time.time()
for i in range(trials):
	if(game.play(black, white) >= 6):
		prob += 1
	
	if(i%10000 == 0):
		endT = time.time()
		print("Loop %d, time(s): %4.3f" % (i,endT-startT))
		print("Running probability: %4.8f" % float(prob/(i+1)))

	game.reset()
	black.reset()
	white.reset()
	

prob = float(prob/trials)	
print("Probability of %d: %4.8f" % (moves,prob))		
