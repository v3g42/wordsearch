import random
import string
import os

class Grid:

	# Constant controlling the prefix rolling while searching in dictionary
	MIN_PREFIX_LENGTH = 2

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


	def _search_in_list(self, words, options = {'pos': 0, 'direction':0, 'x': 0, 'y': 0}):
		"""
		searches every word in the list and returns
		the words present. Takes 2 parameters list of words
		and prefix options which sets the starting point and direction
		"""
		results = []
		for word in words:
			#print(word, pos, x, y)
			result = self.search(word, options)
			if result['success']:
				results.append(word)
		return results


	def search_in_dictionary(self, words):
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
			if len(new_prefix) <= self.MIN_PREFIX_LENGTH:
				if not prefix:
					if self.search(word):
						results.append(word)
				else:
					prefix_result = self.search(prefix)
					if prefix_result['success'] is True:
						if prefix in sub_list: results.append(prefix)
						prefix_optons = {'pos': prefix_result['pos'], 'direction': prefix_result['direction'], 'x': prefix_result['x'], 'y': prefix_result['y']}
						results = results + self._search_in_list(sub_list, prefix_optons)
					prefix = word
					sub_list = [word]
			else:
				prefix = new_prefix
				sub_list.append(word)
		if len(sub_list)>0:
			results = results + self._search_in_list(sub_list)
		return set(results)
