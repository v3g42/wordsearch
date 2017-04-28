#!/usr/bin/env python
import time
import argparse
import multiprocessing
import os
from grid import Grid

MIN_PREFIX_LENGTH = 2

def get_user_input():
	"""
	defines argument parser to take dimensions of the grid
	"""
	parser = argparse.ArgumentParser(
		description='Please provide the dimensions of the grid')
	parser.add_argument(
		'x', metavar='int', type=int, default=10,
		help='x dimension')
	parser.add_argument(
		'y', metavar='int', type=int, default=10,
		help='y dimension')

	args = parser.parse_args()
	return args.x, args.y

def _search_in_list(words, options = {'pos': 0, 'direction':0, 'x': 0, 'y': 0}):
	"""
	searches every word in the list and returns
	the words present. Takes 2 parameters list of words
	and prefix options which sets the starting point and direction
	"""
	results = []
	for word in words:
		#print(word, pos, x, y)
		result = grid.search(word, options)
		if result['success']:
			results.append(word)
	return results

def process_words(words):
	"""
	maintains a rolling prefix till the length becomes less than THRESHOLD
	and calls grid search only if prefix is present
	"""
	results = []
	sub_list = list()
	prefix = None
	for word in words:
		word = word.strip('\n')
		# Check the prefix of sublist so far
		new_prefix = os.path.commonprefix([prefix, word]) if prefix else word
		# if new_prefix length is less than threshold call gridsearch on prefix
		# and if present check for individual strings in sublist
		if len(new_prefix) <= MIN_PREFIX_LENGTH:
			prefix_result = grid.search(prefix)
			if prefix_result['success'] is True:
				if prefix in sub_list: results.append(prefix)
				prefix_optons = {'pos': prefix_result['pos'], 'direction': prefix_result['direction'], 'x': prefix_result['x'], 'y': prefix_result['y']}
				results = results + _search_in_list(sub_list, prefix_optons)
			prefix = word
			sub_list = [word]
		else:
			prefix = new_prefix
			sub_list.append(word)
	return results

if __name__ == '__main__':

	curtime = time.time()
	x, y = get_user_input()
	grid = Grid(x, y)

	# prints the grid to console.
	print('##### Word Grid #####')
	print(grid.to_text())

	print('##### Words #####')
	results = process_words(open('./words.txt'))
	print(results)

	print("Performed in {0} seconds".format(time.time() - curtime))
