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
	fills the grid with random letters
	"""
	def fill(self):
		for p in xrange(self.wid * self.hgt):
				self.data[p] = random.choice(string.lowercase)

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

