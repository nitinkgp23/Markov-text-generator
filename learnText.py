import sys
import json

from generateStats import getNextWordProb


def main():

	if len(sys.argv) != 2:
		print("Exactly 1 argument needed - Path of file containing the text")
		print("Exiting")
		return
	
	text_file = sys.argv[1]
	with open(text_file, 'r') as f:
		text = f.read()

	print("Generating statistics...")
	d = getNextWordProb(text)
	print("Saving generated statistics in a file...")
	with open('stats.json', 'w') as f:
		json.dump(d, f)

	print("Text learnt.")

if __name__ == '__main__':
	main()