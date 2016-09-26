import collections

def swapchars(str):
	counter = collections.Counter(str)
	least = counter.most_common()[-1][0]
	most = collections.Counter(str).most_common()[0][0]
	
	for i in range(len(str)):
		if str[i] == most:
			print least,

		elif str[i] == least:
			print most,
		else:
			print str[i],

swapchars(raw_input())
