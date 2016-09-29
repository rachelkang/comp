results = {}

with open('states.txt', 'r') as f:
	for line in f:
		split_line = line.strip().split(',')
		results[split_line[0]] = split_line[1]

results[split_line[1]] = split_line[0]

def bluesbooze(abbrv):
	return results[abbrv]

print bluesbooze("Illinois")


# def bluesbooze(str):
# 	# locate the state in the abbreviation in the file
# 	text_file = open("states.txt")
# 	states_list = text_file.readlines

# 	# locate the abbreviation
# 	if (state(char + 1) == str(1)) and (state(char + 2) == str(2)):
# 		while (counter < len(state) - 3):
# 			for char in state:
# 				print char - 1

# bluesbooze(raw_input())