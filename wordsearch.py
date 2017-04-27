#!/usr/bin/env python
import time
import argparse
import multiprocessing
import os
#from multiprocessing.dummy import Pool as ThreadPool
from grid import Grid

#pool = ThreadPool(multiprocessing.cpu_count())
#results = pool.map(my_function, my_array)


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

def search_in_list(words):
	"""
	searches every word in the list and returns
	the words present
	"""
	results = []
	for word in words:
		if grid.search(word):
			results.append(word)
	return results

if __name__ == '__main__':
	curtime = time.time()
	x, y = get_user_input()

	grid = Grid(x, y)
	# prints the grid to console.
	print('##### Word Grid #####')
	print(grid.to_text())

	print('##### Words #####')
	results = []

	sub_list = list()
	prefix = ''
	for word in open('./words.txt'):
		word = word.strip('\n')

		if len(prefix) > 0:
			new_prefix = os.path.commonprefix([prefix, word])
			if len(new_prefix) > 2:
				prefix = new_prefix
			else:
				#print(prefix)
				if grid.search(prefix) is True:
					results = results + search_in_list(sub_list)
				sub_list = list()
				prefix = ''
		else:
			prefix = word

		sub_list.append(word)

	print("Performed in {0} seconds".format(time.time() - curtime))
	print(results)




