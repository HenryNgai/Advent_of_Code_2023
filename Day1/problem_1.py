'''
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
'''

import os

def document_parser(document):
	total = 0
	file = open(document, 'r')
	for line in file.readlines(): # O(x) where x is the number of lines
		line_sum = find_line_value(line)
		total = total + line_sum

	return total

def find_line_value(line): 
	p1 = 0
	p2 = len(line) - 1
	char_set = {'1','2','3','4','5','6','7','8','9','0'}

	while line[p1] not in char_set: # Worst case O(n) where n is the numer of chars in the line
		p1+=1

	while line[p2] not in char_set: # Worst case O(n) where n is the numer of chars in the line
		p2-=1 

	return int(line[p1]+line[p2]) # Worst case is O(k^2) where k is the number of digits needed to represent the string


def main():
	# Path of input text file
	data_file_path = os.path.join(os.path.dirname(__file__), 'problem_1_input.txt')
	# Start of processing call
	print(f'Sum of all calibration values: {document_parser(data_file_path)}')

main()

