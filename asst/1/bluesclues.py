results = {}

with open('states.txt', 'r') as f:
	for line in f:
		split_line = line.strip().split(',')
		results[split_line[1]] = split_line[0]

results[split_line[1]] = split_line[0]

def bluesclues(abbrv):
	return results[abbrv]

print bluesclues('IL')

# 	text_file = open("states.txt")
# 	states_list = text_file.readlines

# 	# locate the state in the file
# 	if str == states_list[state]:
# 		for state in states_list:
# 			# locate two letters following comma
# 				# locate comma
# 				# print two characters following comma
# 			if state[char] == ',':
# 				print state(char + 1)
# 				print state(char + 2)

# bluesclues(raw_input())

# with text_file as f: