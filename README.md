### Word Search

Implementation of word search using a dictionary

### Prerequisites

- Python 3
- Pytest

### Sample output
![alt sample_output](https://raw.githubusercontent.com/vivekg342/wordsearch/master/images/sample_output.png)

### Implementation

*grid.py*

Grid is initialized with a [wid*hgt] array.  `grid.fill()` initializes the grid with alphabets randomly.
`letter_index` dictionary stores occurence of every letter in the grid for fast access of first letter.
From a starting point  is performed in all valid directions to see if it matches with the word.

```
Exposes few methods
	- search(word, options)
	 Checks and returns  the positional object of a word in the grid.s

	- search_in_dictionary(words)
	Checks against all the words in the dictionary to find valid words

	- get_next_pos(options)
	Calculates the next position in a word traversal based on current position
	and direction.
```

*wordsearch.py*

Takes user input, initialises a word grid and retrieves all valid words

### Running the application
To create a 15*15 grid
```
./wordsearch.py 15 15
```

Help
```
./wordsearch.py -h
```

### Running unit tests
```
pytest
```



