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

class eCubes(IntEnum):
	RED_CUBES = 12
	GREEN_CUBES = 13
	BLUE_CUBES = 14

def document_parser(document):
	total = 0
	file = open(document, 'r')
	for line in file.readlines(): # O(x) where x is the number of lines		# line_sum = find_line_value(line)
		result = isValidGame(line)
		game_id = extract_game_id(line)
		print(line.rstrip())
		print(f"Game {game_id} {"valid" if result else "invalid"} \n")
		if result:
			total += game_id

	return total

def isValidGame(game):
	game = game.split(':')
	game = game[1].split(';')
	#print(game)
	for draw in game:
		if not isValidDraw(draw):
			return False
	return True
		

def isValidDraw(draw):
	draw = draw.split(',')
	#print(draw)
	for cube in draw:
		if not isValidCube(cube):
			return False
	return True
		

def isValidCube(cube):
	cube = cube.strip()
	cube = cube.split(' ')
	#print(cube)
	value = int(cube[0])
	color = cube[1].lower()

	if color == 'red' and value > eCubes.RED_CUBES:
		print(f"Color: {color} value: {value} is > {eCubes.RED_CUBES}" )
		return False
	elif color =='blue' and value > eCubes.BLUE_CUBES:
		print(f"Color: {color} value: {value} is > {eCubes.RED_CUBES}" ) 
		return False
	elif color == 'green' and value > eCubes.GREEN_CUBES:
		print(f"Color: {color} value: {value} is > {eCubes.RED_CUBES}" )
		return False
	return True


def extract_game_id(line):
	line = line.split(":")[0]
	p1 = 0
	while not line[p1].isdigit():
		p1 += 1

	p2 = p1
	while p2 < len(line):
		if line[p2].isdigit():
			p2 += 1

	if p1 == p2:
		return int(line[p1])
	else:
		return int(line[p1:p2])


def main():
	# Path of input text file
	data_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
	# Start of processing call
	print(f'Sum of all valid game id values: {document_parser(data_file_path)}')

main()