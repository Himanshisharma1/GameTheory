## Himanshi Sharma on Game Theory Pure Nash Equilibrium in 2 x 2 players

##  ______________________
##  p1/p2|	1	 |	2
##  _____|_______|________
##	1	 |(5,5)	 | (1,3)
##  _____|_______|________
##	2	 |(3,1)  | (1,1)
##  _____|_______|________
##
## Equilibrium can be defined as the state where no player has the incentive to change strategy i.e. changing
## strategy would result in lower utility for the player

## Considering only a 2 player game with 2 possibe strategies

possible_outcomes = [(5,5),(1,3),(3,1),(1,1)]
counter = 0
for x in range(2):
	for y in range(2):
		current = possible_outcomes[x][y]
		#Considering player 1 first
		for i in range(2):
			if i == x:
				continue
			else:
				to_compare = possible_outcomes[i][y]
				if to_compare[0] >= current[0]:
					print "current strategy (" + current[0] + "," + current[1] + "is not in Equilibrium"
					breakouter

		#Considering player 1 first
		for j in range(2):
			if j == y:
				continue
			else:
				to_compare = possible_outcomes[x][j]
				if to_compare[1] >= current[1]:
					print "current strategy (" + current[0] + "," + current[1] + "is not in Equilibrium"
					breakouter

		counter += 1
		print "Current strategy (" + current[0] + "," + current[1] + "is an Equilibrium"

if counter == 1:
	print "There is one pure strategy Nash Equilibrium"
else:
	print "There isnt a single pure strategy Equilibrium, the players must play a mixed strategy"
