### Word Search

Implementation of word search using a dictionary

### Implementation

- grid.py  Grid class implementing a word grid
- wordsearch.py reads the dictionary into memory and calls grid search on every word

Grid is initialized with a [wid*hgt] array.  `grid.fill()` initializes the grid with alphabets randomly.
`letter_index` dictionary stores occurence of every letter in the grid for fast access of first letter.

### Running the application
To create a 10*10 grid
```
./wordsearch.py 10 10
```

Help
```
./wordsearch.py -h
```



