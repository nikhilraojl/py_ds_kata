import unittest
from random import random
from ..two_crystal_balls import search

class TestTwoCrystalBalls(unittest.TestCase):
    def test_two_crystal_balls(self):
        ARRAY_RANGE = 1000
        
        idx: int = int(random() * ARRAY_RANGE)
        data: list[bool] = [False for _ in range(ARRAY_RANGE)] 

        for i in range(idx, len(data)):
            data[i] = True

        self.assertEqual(search(data), idx)

        data = [False for _ in range(ARRAY_RANGE)] 
        self.assertEqual(search(data), -1)
