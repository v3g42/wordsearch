import string as string
import unittest
import unittest.mock as mock
from grid import Grid
import pytest


with mock.patch('random.choice', side_effect=list(string.ascii_lowercase[0:12])):
	"""
	Initialises the first 9 alphabets as the grid
	"""
	grid =  Grid(4,3)

def test_get_next_pos_direction():
	"""
	Should return the correct directional characters
	considering the grid starting from center
	a b c d
	e f g h
	i j k l
	"""
	dict = {0: 'j', 1: 'g', 2: 'k', 3: 'c'}
	for direction in range(4):
		x, y = grid.get_next_pos('fat', {'pos': 1, 'direction': direction, 'x': 1, 'y': 1} )
		c = grid.data[grid.wid * y + x]
		assert c == dict[direction]

def test_search_vertical():
	assert grid.search('aei')['success']
	assert grid.search('iea')['success']

def test_search_horizontal():
	assert grid.search('abcd')['success']
	assert grid.search('dcba')['success']

def test_search_diagonal_down():
	assert grid.search('afk')['success']
	assert grid.search('kfa')['success']

def test_search_diagonal_up():
	assert grid.search('ifc')['success']
	assert grid.search('cfi')['success']

def test_search_false():
	assert grid.search('afkl')['success'] == False

def test_invalid_args():
	with pytest.raises(ValueError):
		grid = Grid(0,0)
