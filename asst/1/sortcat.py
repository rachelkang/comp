import collections

# how to indicate imputting as many arguments as possible?
def sortcat(*arg):	
	# do i need to make sure n is an int?	
	n = arg[0]
	
	# push arguments into a list, except for first one
	sortcat_list = arg
	sortcat_list.remove(arg[0])

	# loop
		# find longest argument . . . until iterations = n
			# print each time going through loop
		# some sort of counter for number of iterations?
	while (counter < n + 1):
		for elt in sortcat_list:
			max = max(sortcat_list)
			print max
		counter = counter + 1

sortcat(raw_input())