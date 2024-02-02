# A port of ThePrimeagen's kata-machine to python
Used in [The Last Algorithms Course You'll Need](https://frontendmasters.com/courses/algorithms/]) on Frontend Masters

## WIP not all DS and Algos from the course are added
[Github link](https://github.com/ThePrimeagen/kata-machine) to original repo

## Why?
The kata-machine is in Js/Ts, I just wanted to have something similar in python for practicing. Hence the reason solutions are not present :)

## Usage
- Required to have python 3.12(type hints features introduced in this version are used)
- Clone this repo, write implementations for any of data structures and algorithms in `src` directory
- Run test for a specific implementation using `unittest` module in python. Example
```shell
# Running tests for src/linear_search.py
python -m unittest src.test.test_linear_search # with full path to the test

# or simply
python -m unittest -k linear

# NOTE: Tests should be run from root of the project as cwd
```
### suggested order
- Linear search
- Binary search
- Two Crystal Balls O(sqrt(N))
- Queue
- Stack
- Bubble sort
- Quick sort
- Singly linked list
- Doubly linked list
- Binary trees
  - Traversal
    - pre-order
    - in-order (depth-first)
    - pre-order
    - breadth-first
  - Search
    - depth-first
    - breadth-first
    
