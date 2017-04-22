import random
import string

class Grid:
	def __init__(self, wid, hgt):
		self.wid = wid
		self.hgt = hgt
		self.data = [None] * (wid * hgt)
		self.fill()


	def to_text(self):
		result = []
		for row in xrange(self.hgt):
			result.append(' '.join(self.data[row * self.wid :(row + 1) * self.wid]))

		return '\n'.join(result)

	def fill(self):
		for p in xrange(self.wid * self.hgt):
				self.data[p] = random.choice(string.lowercase)

	def combinations(self):
		return

