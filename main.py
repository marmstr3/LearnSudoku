#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes an unsolved sudoku puzzle and solves it
"""
# Created on Mon Dec 23 2019
# Author: Michael Armstrong

import json
import SudokuObjects
                
# Get Puzzle from json file
with open('tests/test_objects.json') as f:
    test_objects = json.load(f)
puzzle = test_objects['puzzles']['test puzzles']['solvable without exclusion']

# Temporary puzzle for testing
sudoku = SudokuObjects.SudokuPuzzle(puzzle)
counter = 0

while not sudoku.is_solved and counter < 100:
    sudoku.update_coordinates()
    sudoku.check_if_solved()
    counter += 1
