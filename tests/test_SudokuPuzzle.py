#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 07:37:32 2020

@author: Michael
"""

import unittest
import json
from SudokuObjects import SudokuPuzzle

# Initialize Test Puzzles
with open('test_objects.json') as f:
    test_objects = json.load(f)
test_puzzles = test_objects['puzzles']['test puzzles']

class GetReadableBoardTestCase(unittest.TestCase):
    """
    Tests the get_readable_board() method for the SudokuObjects.SudokuPuzzle
    class
    """
    def test_initial_board(self):
        puzzle = test_puzzles['solvable without exclusion']
        test_puzzle = SudokuPuzzle(puzzle)
        readable_board = test_puzzle.get_readable_board()
        correct_value = [[0, 6, 0, 3, 0, 0, 8, 0, 4],
                         [5, 3, 7, 0, 9, 0, 0, 0, 0],
                         [0, 4, 0 ,0, 0, 6, 3, 0, 7],
                         [0, 9, 0, 0, 5, 1, 2, 3, 8],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [7, 1, 3, 6, 2, 0, 0, 4, 0],
                         [3, 0, 6, 4, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 6, 0, 5, 2, 3],
                         [1, 0, 2, 0, 0, 9, 0, 8, 0]
                         ]  
        self.assertEqual(readable_board, correct_value)
        
unittest.main()
        