import numpy as np
import json
import time
import sys

def getNextWord(word, d):
	possible_words = d.get(word, None)
	if possible_words is None:
		print("OOV word encountered")
		return
	return np.random.choice(list(possible_words.keys()), p=list(possible_words.values()))

def main():

	if len(sys.argv) > 2:
		print("Max 1 argument needed - A word to begin with")
		print("Exiting")
		return
	
	elif len(sys.argv) == 2:
		curr_w = sys.argv[1]

	else:
		curr_w = 'The'

	try:
		with open('stats.json', 'r') as f:
			d = json.load(f)

	except:
		print('Text not learnt. Please run learnText.py first')
		print('Exiting')
		return

	text = [curr_w]
	num_words = 1000
	while num_words >0:
		curr_w = getNextWord(curr_w, d)
		text.append(curr_w)
		num_words -= 1
	
	for w in text:
		print(w, end=' ')
		# time.sleep(0.3)

if __name__ == '__main__':
	main()