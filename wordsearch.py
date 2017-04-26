#!/usr/bin/env python

from grid import Grid

if __name__ == '__main__':

	words = [word.strip('\n') for word in open('./words.txt')]
	grid = Grid(4, 3)

	# prints the grid to console.
	print(grid.to_text())

	results = []
	# Checks word against every combination available
	for combination in grid.combinations():
		for word in words:
			if(combination.find(word)>-1):
				results.append(word)
				print(combination, word)





