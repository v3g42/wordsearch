import random
import string


class Grid:

	def __init__(self, wid, hgt):
		"""
		Initializes the grid and fills with random letters
		"""
		self.wid = wid
		self.hgt = hgt
		self.data = [None] * (wid * hgt)
		self.letter_index = {l: [] for l in string.lowercase}
		self.fill()

	def to_text(self):
		"""
		Converts the grid in human readable format.
		"""
		result = []
		for row in xrange(self.hgt):
			result.append(' '.join(self.data[row * self.wid :(row + 1) * self.wid]))

		return '\n'.join(result)

	def fill(self):
		"""
		Fills the grid with random letters and stores
		"""
		for p in xrange(self.wid * self.hgt):
				random_letter = random.choice(string.lowercase)
				self.data[p] = random_letter
				self.letter_index[random_letter].append(p)


	def _get_next_pos(self, word, pos, direction, x, y):
		"""
		Calculates the next position based on direction parameter
		(0: horizontal, 1: vertical, 2: left diagonal, 3: right diagonal)
		"""
		dimension, increment = divmod(direction, 4)
		increment  = -1 if increment > 4 else 1
		if dimension == 0:
			y = y + 1
		elif dimension == 1:
			x = x + 1
		elif dimension == 2:
			x = x + 1
			y = y + 1
		elif dimension == 3:
			x = x + 1
			y = y - 1
		return x,y

	def _search_in_direction(self, word, direction, pos=0, x=0, y=0):
		"""
		Recursively checks for word traversing in four possible directions
		"""
		# When pos=0 computes the starting point in the search.
		if pos == 0:
			arr = self.letter_index[word[0]]
			if len(arr)==0: return False

			# calls search on every available position of this alphabet
			for coord in arr:
		  		y, x = divmod(coord, self.wid)
		  		if self._search_in_direction(word, direction, pos+1, x, y): return True
		  	return False
		else:
			# Comptes the next position
			x, y = self._get_next_pos(word, pos, direction, x, y)
			# Returns False if out of bounds
			if x < 0  or x >= self.wid or y<0  or y >= self.hgt: return False
			# Returns False if positional alphabet doesn't match
			if word[pos] != self.data[y*self.wid + x]: return False
			# If all alphabets match return True
			if pos == len(word)-1: return True
			return self._search_in_direction(word, direction, pos+1, x, y)



	def search(self, word):
		"""
		searches the grid for a specific word in a DFS fashion
		"""
		exists = False
		for direction in xrange(8):
			if self._search_in_direction(word, direction) or self._search_in_direction(word[::-1], direction):
				return True
		return False

