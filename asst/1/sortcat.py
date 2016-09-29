def sortcat(*args):		
	
	print args

	n = args[0]
	
	sortcat_list = list(args)
	sortcat_list.remove(args[0])

	sortcat_list.sort(key=len, reverse=True)

	largest_args = sortcat_list[:n]

	result = ''

	for arg in largest_args:
		result += arg

	print result

sortcat(2, 'aaaaaaaaaa', 'cccc', 'd', 'bbbbbbb')


	# loop
		# find longest argument . . . until iterations = n
			# print each time going through loop
		# some sort of counter for number of iterations?
	# while (counter < n + 1):
	# 	for elt in sortcat_list:
	# 		max = max(sortcat_list)
	# 		print max
	# 	counter = counter + 1

# sortcat(raw_input())