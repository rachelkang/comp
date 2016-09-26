def bluesbooze(str):
	# locate the state in the abbreviation in the file
	text_file = open("states.txt")
	states_list = text_file.readlines

	# locate the abbreviation
	if (state(char + 1) == str(1)) and (state(char + 2) == str(2)):
		while (counter < len(state) - 3):
			for char in state:
				print char - 1

bluesbooze(raw_input())