#!/usr/bin/env python
import time
import argparse
from grid import Grid

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


if __name__ == '__main__':

	curtime = time.time()
	x, y = get_user_input()
	grid = Grid(x, y)

	# prints the grid to console.
	print('##### Word Grid #####')
	print(grid.to_text())

	print('##### Words #####')
	results = grid.search_in_dictionary(open('./words.txt'))
	print(results)

	print("Performed in {0} seconds".format(time.time() - curtime))
