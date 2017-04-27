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

### Sample output
```
##### Word Grid #####
d l p z w n f e h t d d p v l
x m o i f w s h l o y b n i z
r w l p z e i e z o z e y p y
n c x z o h u s t c v g b p u
f y a v k d j s s r l l s e s
y k k d p l e b t u v z y l s
z d s j n h r k v t y c q n a
t u j h q x f j z o i j a o p
y v l f l s j m s x r q s x j
x t d k f w x x g o h z k d g
s e f i k f z q c x c v d o g
g r j s o y t i y w k b c u l
k a u a k j z u a u c g g i t
y d w y p h u j m w f k b a w
g k s b i a m l k g m v j t g
##### Words #####
['ad', 'ah', 'am', 'an', 'are', 'as', 'as', 'ask', 'ass', 'at', 'ax', 'ay', 'be', 'beg', 'by', 'cad', 'cog', 'coo', 'cs', 'do', 'dog', 'due', 'eh', 'era', 'es', 'ex', 'gag', 'go', 'god', 'gs', 'ha', 'he', 'hes', 'hes', 'hew', 'hi', 'ho', 'hog', 'icy', 'id', 'if', 'ifs', 'in', 'is', 'is', 'it', 'it', 'jaw', 'jay', 'jut', 'kc', 'ks', 'la', 'lib', 'lo', 'lop', 'ls', 'ma', 'may', 'ms', 'mu', 'no', 'ode', 'of', 'oh', 'on', 'or', 'ow', 'own', 'ox', 'pa', 'pas', 'pas', 'pi', 'pod', 'pol', 're', 'rs', 'rs', 'rut', 'sap', 'say', 'set', 'sh', 'sly', 'so', 'soy', 'spy', 'sue', 'the', 'ti', 'to', 'to', 'too', 'toy', 'ts', 'uh', 'um', 'up', 'us', 'wag', 'we', 'yam', 'ye', 'yip', 'yo', 'zip']
Performed in 0.344338178635 seconds

```

