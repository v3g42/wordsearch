import random
import string


class Grid:
	"""
	initializes the grid and fills with random letters
	"""
	def __init__(self, wid, hgt):
		self.wid = wid
		self.hgt = hgt
		self.data = [None] * (wid * hgt)
		self.letter_index = {l: [] for l in string.lowercase}
		self.fill()


	"""
	converts the grid in human readable format.
	"""
	def to_text(self):
		result = []
		for row in xrange(self.hgt):
			result.append(' '.join(self.data[row * self.wid :(row + 1) * self.wid]))

		return '\n'.join(result)

	"""
	fills the grid with random letters and stores
	"""
	def fill(self):
		for p in xrange(self.wid * self.hgt):
				random_letter = random.choice(string.lowercase)
				self.data[p] = random_letter
				self.letter_index[random_letter].append(p)


	def _get_next_pos(self, word, pos, direction, x, y):
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

		# Initalize coordinates and call search
		if pos == 0:
			arr = self.letter_index[word[0]]
			if len(arr)==0: return False

			for coord in arr:
		  		y, x = divmod(coord, self.wid)
		  		if self._search_in_direction(word, direction, pos+1, x, y): return True
		  	return False
		else:
			x, y = self._get_next_pos(word, pos, direction, x, y)
			if x < 0  or x >= self.wid or y<0  or y >= self.hgt: return False
			if word[pos] != self.data[y*self.wid + x]: return False
			if pos == len(word)-1: return True
			return self._search_in_direction(word, direction, pos+1, x, y)


	"""
	searches the grid for a specific word in a DFS fashion
	"""
	def search(self, word):
		exists = False
		for direction in xrange(8):
			if self._search_in_direction(word, direction) or  self._search_in_direction(word[::-1], direction):
				return True
		return False

	"""
	returns all valid combinations in the grid.
	"""
	def combinations(self):
		all_results = []

		# horizontal combinations
		results = []
		for y in xrange(self.hgt):
			str = ''
			for x in xrange(self.wid):
				str = str + self.data[y*self.wid + x]
			results.append(str)
		all_results = all_results + results

		# vertical combinations
		results = []
		for x in xrange(self.wid):
			str = ''
			for y in xrange(self.hgt):
				str = str + self.data[y*self.wid + x]
			results.append(str)

		all_results = all_results + results


		#  left diagonal combinations
		results = []
		steps = self.hgt + self.wid - 1
		for d in xrange(steps):
			z1  =  0 if d < self.wid else d - self.wid + 1
			z2  =  0 if d < self.hgt else d - self.hgt + 1
			str = ''
			for j in xrange(z1, d-z2+1):
				str = str + self.data[(d-j) + j * self.wid]
			if len(str)>1: results.append(str)

		all_results = all_results + results

		# right diagonal combinations
		results = []
		steps = self.hgt + self.wid - 1
		for d in xrange(steps):
			z1  =  0 if d < self.wid else d - self.wid + 1
			z2  =  0 if d < self.hgt else d - self.hgt + 1
			str = ''
			for j in xrange(z1, d-z2+1):
				str = str + self.data[(d-j) + (self.hgt-j-1) * self.wid]

			if len(str)>1:  results.append(str)

		all_results = all_results + results

		# all possible values can also be present in the reverse order
		all_results = all_results +  [s[::-1] for s in all_results]

		return all_results

