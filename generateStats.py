
def getCounts(text):
	'''
	Takes in some text, and returns a dict with keys as 'word' and value as {nextword:count}
	'''
	d = {}
	words = text.split()
	for i in range(len(words)-1):
		curr_w = words[i]
		next_w = words[i+1]
		if curr_w in d.keys():
			if next_w in d[curr_w].keys():
				d[curr_w][next_w] += 1
			else:
				d[curr_w][next_w] = 1
		else:
			d[curr_w] = {}
			d[curr_w][next_w] = 1

	return d


def getNextWordProb(text):
	'''
	'''
	d = getCounts(text)
	nextWord = {}
	for key, value in d.items():
		totalCount = sum(value.values())
		nextWord[key] = {k: v/totalCount for k,v in value.items()}
	
	return nextWord
