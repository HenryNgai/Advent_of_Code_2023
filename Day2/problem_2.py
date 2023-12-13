'''
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''


import os

from enum import IntEnum, Enum

class eTUPLE_IDX(IntEnum):
	RED_CUBES = 0
	GREEN_CUBES = 1
	BLUE_CUBES = 2


def document_parser(document):
	total = 0
	file = open(document, 'r')
	for line in file.readlines(): # O(x) where x is the number of lines		# line_sum = find_line_value(line)
		print(f"{line.rstrip()}")
		result = decomposeGame(line.rstrip())
		answer = result[eTUPLE_IDX.RED_CUBES] * result[eTUPLE_IDX.GREEN_CUBES] * result[eTUPLE_IDX.BLUE_CUBES]
		print(f"Result {result} and {answer}\n" )
		total += answer

		

	return total

def decomposeGame(game):
	max_red = 0
	max_blue = 0
	max_green = 0

	game = game.split(':')
	game = game[1].split(';')
	for draw in game:
		result = decomposeDraw(draw)
		max_red = max(result[eTUPLE_IDX.RED_CUBES],max_red)
		max_blue = max(result[eTUPLE_IDX.BLUE_CUBES], max_blue)
		max_green = max(result[eTUPLE_IDX.GREEN_CUBES], max_green)

	return ((max_red,max_blue,max_green))

		

def decomposeDraw(draw):
	red = 0
	blue = 0
	green = 0
	draw = draw.split(',')
	for cube in draw:
		result = decomposeCube(cube)
		
		if result[0] == 'red':
			red = result[1]
		if result[0] == 'blue':
			blue = result[1]
		if result[0] == 'green':
			green = result[1]

	return ((red,blue,green))
		

def decomposeCube(cube):
	cube = cube.strip()
	cube = cube.split(' ')
	value = int(cube[0])
	color = cube[1].lower()

	return((color,value))



def main():
	# Path of input text file
	data_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
	# Start of processing call
	print(f'Sum of all power: {document_parser(data_file_path)}')

main()