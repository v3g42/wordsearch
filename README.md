### Word Search

Implementation of word search using a dictionary

### Prerequisites

- Python 3
- Pytest

### Implementation

- grid.py  Grid class implementing a word grid

Grid is initialized with a [wid*hgt] array.  `grid.fill()` initializes the grid with alphabets randomly.
`letter_index` dictionary stores occurence of every letter in the grid for fast access of first letter.
From a starting point  is performed in all valid directions to see if it matches with the word.

- wordsearch.py reads the dictionary into memory and calls grid search on every word

Combines multiple words with a common prefix and checks if prefix is present and thereafter individual words


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


