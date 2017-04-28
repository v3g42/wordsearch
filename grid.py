import random
import string

class Grid:

	def __init__(self, wid, hgt):
		"""
		Initializes the grid and fills with random letters
		"""
		if wid <=0 or hgt <=0:
			raise ValueError('wid and hgt need to be positive integers')
		self.wid = wid
		self.hgt = hgt
		self.data = [None] * (wid * hgt)
		self.letter_index = {l: [] for l in string.ascii_lowercase}
		self._fill()

	def to_text(self):
		"""
		Converts the grid in human readable format.
		"""
		result = []
		for row in range(self.hgt):
			result.append(' '.join(self.data[row * self.wid :(row + 1) * self.wid]))

		return '\n'.join(result)

	def _fill(self):
		"""
		Fills the grid with random letters and stores
		index of all stored alphabets
		"""
		for p in range(self.wid * self.hgt):
				random_letter = random.choice(string.ascii_lowercase)
				self.data[p] = random_letter
				self.letter_index[random_letter].append(p)


	def get_next_pos(self, word, options={'pos': 0, 'direction':0, 'x': 0, 'y': 0}):
		"""
		Calculates the next position based on direction parameter
		(0: vertical, 1: horizontal, 2: diagonal down, 3: diagonal up)
		"""
		pos = options['pos']
		x = options['x']
		y = options['y']
		direction = options['direction']
		increment, dimension  = divmod(direction, 4)
		increment  = -1 if increment > 0 else 1
		if dimension == 0:
			y = y + increment
		elif dimension == 1:
			x = x + increment
		elif dimension == 2:
			x = x + increment
			y = y + increment
		elif dimension == 3:
			x = x + increment
			y = y - increment
		return x,y

	def _search_in_direction(self, word, options={'pos': 0, 'direction':0, 'x': 0, 'y': 0}):
		"""
		Recursively checks for word traversing in four possible directions.
		Takes paramter word and options for starting point
		"""
		pos = options['pos']
		direction = options['direction']

		# Comptes the next position
		x, y = self.get_next_pos(word, options)

		# Returns False if out of bounds
		if x < 0 or x >= self.wid or y<0  or y >= self.hgt:
			return {'success':False, 'pos': -1, 'x': -1, 'y': -1, 'direction': direction}

		# Returns False if positional alphabet doesn't match
		if word[pos] != self.data[y*self.wid + x]:
			return {'success':False, 'pos': -1, 'x': -1, 'y': -1, 'direction': direction}

		# If all alphabets match return True
		if pos == len(word)-1:
			return {'success':True, 'pos': pos, 'x': x, 'y': y, 'direction': direction}

		return self._search_in_direction(word, {'pos': pos+1, 'direction':direction, 'x': x, 'y': y})

	def search(self, word, options={'pos': 0, 'direction':0, 'x': 0, 'y': 0}):
		"""
		searches the grid for a specific word in a DFS fashion
		"""
		pos = options['pos']
		if pos == 0:
			arr = self.letter_index[word[0]]
			if len(arr)==0: return {'success':False, 'pos': -1, 'x': -1, 'y': -1, 'direction': -1}
			for coord in arr:
				y, x = divmod(coord, self.wid)
				for direction in range(8):
					result = self._search_in_direction(word, {'pos': 1, 'direction':direction, 'x': x, 'y': y})
					if result['success']:
						return result
			return {'success':False, 'pos': -1, 'x': -1, 'y': -1, 'direction': -1}
		else:
			return self._search_in_direction(word, options)
