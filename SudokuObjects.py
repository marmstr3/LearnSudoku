#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:08:45 2019

@author: Michael
"""

import numpy as np

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
        
    Methods:
        - get_cant_be_vector_count
        - check_if_coordinate_solved
        - set_initial_coordinate_is_solved
        - set_initial_cant_be
        - set_cant_be
    """
    
    def __init__(self, sudoku_board):
        self.is_solved = False
        self.set_initial_sudoku_board(sudoku_board)

    def set_initial_sudoku_board(self, sudoku_board):
        self.sudoku_board = np.empty((9,9))
        for row_coordinate in range(9):
            for column_coordinate in range(9):
                coordinate_value = sudoku_board[row_coordinate, column_coordinate]
                self.sudoku_board[row_coordinate, column_coordinate] = SudokuCoordinate(coordinate_value, (row_coordinate, column_coordinate))
    
    def set_initial_cant_be(self):
        for coordinate in np.nditer(self.sudoku_board):
            coordinate.set_initial_cant_be
    
    def set_cant_be(self):
        for row_coordinate in range(9):
            for column_coordinate in range(9):
                if not self.coordinate_is_solved[row_coordinate, column_coordinate]:
                    for n in range(9):
                        if (n + 1) in self.sudoku_board[row_coordinate, :]:
                            self.cant_be[row_coordinate, column_coordinate, n] = True
                        elif (n + 1) in self.sudoku_board[:, column_coordinate]:
                            self.cant_be[row_coordinate, column_coordinate, n] = True
                            
                            
class SudokuCoordinate():
    def __init__(self, coordinate_value, location):
        self.value = coordinate_value
        self.location = location
        self.set_initial_cant_be()
    
    def set_initial_cant_be(self):
        if self.value:
            self.cant_be = np.full((9), 1, dtype=bool)
            self.cant_be[self.value - 1] = False
        else:
            self.cant_be = np.zeros((9), dtype=bool)
    
    def check_if_coordinate_solved(self):
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
                    
    def update_cant_be(self, row, column, region):
        """
        Inputs:
            - row: 1x9 Numpy Array; The full row that the coordinate is a member of
            - column: 9x1 Numpy Array; The full column that the coordinate is a member of
            - region: 3x3 Numpy Array; The region that the coordinate is a member of
        """
        flattened_region = region.flatten()
        for n in range(9):
        # If the cant_be property for this entry has not been determined yet
            # Check Row
            if row[n].value:
                row_value = row[n].value
                self.cant_be[row_value - 1] = True
            # Check Column
            if column[n].value:
                column_value = column[n].value
                self.cant_be[column_value - 1] = True
            # Check Region
            if flattened_region[n].value:
                region_value = flattened_region[n].value
                self.cant_be[region_value - 1] = True
        # N-Exclusion
        