'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''


import os

def document_parser(document):
	count = 0
	total = 0
	file = open(document, 'r')
	for line in file.readlines(): w
		nums_in_line = find_line_nums(line)
		strings_in_line = find_line_strings(line)
		result = nums_in_line + strings_in_line
		print(result)

		current_min = len(line)
		current_min_val = None
		current_max = -1
		current_max_val = None
		for i in range (len(result)):
			if result[i][0] != -1 and result[i][1] != '-1':
				if result[i][0] < current_min:
					current_min = result[i][0]
					current_min_val = result[i][1]
				if result[i][0] > current_max:
					current_max = result[i][0]
					current_max_val = result[i][1]
		count+=1
		print(f"line:{count} {int(current_min_val+current_max_val)}")
		total = total + int(current_min_val+current_max_val)

	return total



def find_line_strings(line):
	word_int_dict = {"one": "1", "two" : "2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0", " ":"-1"}

	min_index = len(line)
	min_word = ' '

	for word in word_int_dict.keys():
		result = line.find(word)
		if result != -1:
			if result < min_index:
				min_index = result
				min_word = word

	max_index = -1
	max_word = ' '

	for word in word_int_dict.keys():
		result = line.rfind(word)
		if result != -1:
			if result > max_index:
				max_index = result
				max_word = word

	return[(min_index,word_int_dict[min_word]), (max_index,word_int_dict[max_word])]


def find_line_nums(line): 
	p1 = 0
	p2 = len(line) - 1
	char_set = {'1','2','3','4','5','6','7','8','9','0'}

	while line[p1] not in char_set: # Worst case O(n) where n is the numer of chars in the line
		p1+=1

	while line[p2] not in char_set: # Worst case O(n) where n is the numer of chars in the line
		p2-=1 

	return [(p1, line[p1]),(p2,line[p2])] #Return indicies of first and last number




def main():
	# Path of input text file
	data_file_path = os.path.join(os.path.dirname(__file__), 'problem_1_input.txt')
	# Start of processing call
	print(f'Sum of all calibration values: {document_parser(data_file_path)}')

main()
