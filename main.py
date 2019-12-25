#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes an unsolved sudoku puzzle and solves it
"""
# Created on Mon Dec 23 2019
# Author: Michael Armstrong

import SudokuObjects
                

# Temporary puzzle for testing
sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ]
                

sudoku = SudokuObjects.SudokuPuzzle(sudoku_board)
while not sudoku.is_solved and counter < 100:
    sudoku.update_cant_be()

