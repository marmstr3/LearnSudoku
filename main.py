#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes an unsolved sudoku puzzle and solves it
"""
# Created on Mon Dec 23 2019
# Author: Michael Armstrong

import SudokuObjects
                

# Temporary puzzle for testing
sudoku_board = [[0, 6, 0, 3, 0, 0, 8, 0, 4],
                [5, 3, 7, 0, 9, 0, 0, 0, 0],
                [0, 4, 0 ,0, 0, 6, 3, 0, 7],
                [0, 9, 0, 0, 5, 1, 2, 3, 8],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [7, 1, 3, 6, 2, 0, 0, 4, 0],
                [3, 0, 6, 4, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 6, 0, 5, 2, 3],
                [1, 0, 2, 0, 0, 9, 0, 8, 0]
                ]
                

sudoku = SudokuObjects.SudokuPuzzle(sudoku_board)
counter = 0

while not sudoku.is_solved and counter < 100:
    sudoku.update_coordinates()
    sudoku.check_if_solved()
    counter += 1
    print(counter)
