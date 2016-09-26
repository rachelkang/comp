def abbrv(str):
	
	text_file = open("states.txt")
	states_list = text_file.readlines

	# locate the state in the file
	if str == states_list[state]:
		for state in states_list:
			# locate two letters following comma
				# locate comma
				# print two characters following comma
			if state[char] == ',':
				print state(char + 1)
				print state(char + 2)

abbrv(raw_input())