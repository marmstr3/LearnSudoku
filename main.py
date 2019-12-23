#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes an unsolved sudoku puzzle and solves it
"""
# Created on Mon Dec 23 2019
# Author: Michael Armstrong

import numpy as np

# Temporary puzzle for testing
sudoku_board = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                         [6, 0, 0, 1, 9, 5, 0, 0, 0],
                         [0, 9, 8, 0, 0, 0, 0, 6, 0],
                         [8, 0, 0, 0, 6, 0, 0, 0, 3],
                         [4, 0, 0, 8, 0, 3, 0, 0, 1],
                         [7, 0, 0, 0, 2, 0, 0, 0, 6],
                         [0, 6, 0, 0, 0, 0, 2, 8, 0],
                         [0, 0, 0, 4, 1, 9, 0, 0, 5],
                         [0, 0, 0, 0, 8, 0, 0, 7, 9]
                         ]
                        )

class SudokuPuzzle():
    """
    Attributes:
        - is_solved: Boolean; Remains 'False' until puzzle is solved.
        
        - sudoku_board: Numpy Array, Integer; A 9x9 array the current state of  
        the sudoku puzzle.
        
        - cant_be: Numpy Array, Boolean; 9x9x9 array where the first 2 
        coordinates are the coordinates in the puzzle, and the last coordinate
        represents the possible values (1 through 9) for the location in the p
        puzzle. A True in any location means that the corresponding value cannot
        be used at this location in the puzzle.
        
        - coordinate_is_solved: Numpy Array, Boolean; 9x9 array that represents 
        each location on the board. A True value means the corresponding 
        location has been solved for.
    """
    
    def __init__(self, sudoku_board):
        self.is_solved = False
        self.sudoku_board = sudoku_board
        self.cant_be = np.zeros((9,9,9), dtype=bool)
        self.coordinate_is_solved = np.zeros((9,9), dtype=int)

    
    def get_cant_be_vector_count(self, row_coordinate, column_coordinate):
        cant_be_vector = self.cant_be[row_coordinate, column_coordinate]
        counter = 0
        for n in range(0,9):
            if cant_be_vector[n]:
                counter += 1
        
        return counter
            
    def check_if_solved(self):
        for row_coordinate in range(9):
            for column_coordinate in range(9):
                vector_count = self.get_cant_be_vector_count(row_coordinate, column_coordinate)
                if vector_count == 8:
                    self.coordinate_is_solved[row_coordinate, column_coordinate] = True
                elif vector_count > 0 and vector_count < 8:
                    self.coordinate_is_solved[row_coordinate, column_coordinate] = False
                else:
                    error = 'Error in SudokuPuzzle.check_if_solved. Count of '
                    error += 'possible cant_be values is outside of '
                    error += 'the expected range. Expected a value between 0 '
                    error += 'and 8. Got ' + str(vector_count) + '.'
                    raise ValueError(error)
                
                
    
    def set_cant_be(self):
        for row_coordinate in range(9):
            for column_coordinate in range(9):
                if self.sudoku_board[row_coordinate, column_coordinate]:
                    self.cant_be = []
                for n in range(9):
                    if (n + 1) in self.sudoku_board[row_coordinate, :]:
                        self.cant_be[row_coordinate, column_coordinate, n] = 1
                    elif (n + 1) in self.sudoku_board[:, column_coordinate]:
                        self.cant_be[row_coordinate, column_coordinate, n] = 1
                

