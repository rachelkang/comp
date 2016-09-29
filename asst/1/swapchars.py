import collections

def swapchars(message):
	counter = collections.Counter(message)
	least = counter.most_common()[-1][0]
	most = collections.Counter(message).most_common()[0][0]
	
	output = ''

	for i in range(len(message)):
		if message[i] == most:
			output += least
		elif message[i] == least:
			output += most
		else:
			output += message[i]

	print output

swapchars(raw_input())