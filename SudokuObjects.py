#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:08:45 2019

@author: Michael
"""
import copy


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


    @staticmethod
    def check_shape_is_even(sudoku_board, number_of_columns):
        for row in sudoku_board:
            specific_number_of_columns = len(row)
            if specific_number_of_columns != number_of_columns:
                error = "Input rows are not all the same length. Please check "
                error += "your input and try again.\nSource: SudokuPuzzle."
                error += "check_shape_is_even"
                raise ValueError(error)
            else:
                return True

    def get_readable_board(self):
        # initialize board
        readable_board = []
        for n in range(9):
            row = []
            for m in range(9):
                row.append(0)
            readable_board.append(row)
        
        # put in values for board
        for n in range(9):
            for m in range(9):
                value = self.sudoku_board[n][m].value
                readable_board[n][m] = value
        
        return readable_board

    def iterable_sudoku_board(self):
        iterable_sudoku_board = copy.copy(self.sudoku_board[0])
        for n in range(1,9):
            iterable_sudoku_board += copy.copy(self.sudoku_board[n])
            
        return iterable_sudoku_board

    def get_sudoku_board_shape(self, sudoku_board):
        number_of_rows = len(sudoku_board)
        number_of_columns = len(sudoku_board[0])
        if self.check_shape_is_even(sudoku_board, number_of_columns):
            return (number_of_rows, number_of_columns)
        
    def check_if_values_in_range(self, sudoku_board):
        for n in range(9):
            max_value = max(sudoku_board[n])
            min_value = min(sudoku_board[n])
            if min_value < 0:
                error = "Negative input value found. Please check your input "
                error += "and try again.\nSource:SudokuPuzzle.set_initial_"
                error += "sudoku_board"
                raise ValueError(error)
            elif max_value > 9:
                error = "Value greater than 9 found. Please check your input "
                error += "and try again.\nSource:SudokuPuzzle.set_initial_"
                error += "sudoku_board"
        
    def check_sudoku_board_input(self, sudoku_board):
        if type(sudoku_board) is not list:
            error = "Input is not a list. Please check your input and try "
            error += "again.\nSource: SudokuPuzzle.set_initial_sudoku_board"
            raise ValueError(error)
        elif self.get_sudoku_board_shape != (9,9):
            error = "Input is not 9x9. Please check your input and try again."
            error += "\nSource: SudokuPuzzle.set_initial_sudoku_board"
            
        self.check_if_values_in_range(sudoku_board)

    def initialize_sudoku_board(self):
        self.sudoku_board = []
        for n in range(9):
            self.sudoku_board.append([0]*9)

    def get_coordinate(self, row_coordinate, column_coordinate):
        coordinate = self.sudoku_board[row_coordinate][column_coordinate]
        return coordinate

    def set_initial_sudoku_board(self, sudoku_board):
        self.check_sudoku_board_input(sudoku_board)
        self.initialize_sudoku_board()
        for row_coordinate in range(9):
            for column_coordinate in range(9):
                coordinate_value = sudoku_board[row_coordinate][column_coordinate]
                self.sudoku_board[row_coordinate][column_coordinate] = SudokuCoordinate(coordinate_value, (row_coordinate, column_coordinate))
    
    def set_cant_be(self):
        for row_coordinate in range(9):
            for column_coordinate in range(9):
                if not self.coordinate_is_solved[row_coordinate, column_coordinate]:
                    for n in range(9):
                        if (n + 1) in self.sudoku_board[row_coordinate, :]:
                            self.cant_be[row_coordinate, column_coordinate, n] = True
                        elif (n + 1) in self.sudoku_board[:, column_coordinate]:
                            self.cant_be[row_coordinate, column_coordinate, n] = True
                      
    def get_region(self, row_number, column_number):
        # Floor divide to get index of region and then multiply by 3 to get 
        # first column/row of region
        initial_row = int(row_number/3)*3
        initial_column = int(column_number/3)*3
        region = []
        for n in range(3):
            for m in range(3):
                loop_row = n + initial_row
                loop_column = m + initial_column
                region.append(self.sudoku_board[loop_row][loop_column])
        return region
    
    def get_row(self, row_number):
        row = self.sudoku_board[row_number]
        return row
    
    def get_column(self, column_number):
        column = []
        for n in range(9):
            column.append(self.sudoku_board[n][column_number])
        return column
    
    def update_coordinates(self):
        for coordinate in self.iterable_sudoku_board():
            row_number = coordinate.location[0]
            column_number = coordinate.location[1]
            row = self.get_row(row_number)
            column = self.get_column(column_number)
            region = self.get_region(row_number, column_number)
            coordinate.update_cant_be(row, column, region)
            coordinate.update_value()
        
    def check_if_solved(self):
        solved_tracker = True
        for coordinate in self.iterable_sudoku_board():
            if not coordinate.value:
                solved_tracker = False
                break
        self.is_solved = solved_tracker
        
    
                            
class SudokuCoordinate():
    """
    Attributes:
        - value: Integer; The value for this coordinate on the sudoku board. 0
        if the value is unknown.
        - location: 2x1 Tuple; The coordinate location on the sudoku board.
        coordinate on the sudoku board. (row_coordinate, column_coordinate).
        - cant_be: 9x1 Numpy Array, Boolean; Represents the possible values for this 
        coordinates (1 through 9). A value of True in a given space means 
        that the respective value is not a valid candidate for the value of the 
        coordinate.
        - solved: Boolean; Flag for whether or not the value for this 
        coordinate has been solved for.
    """
    
    def __init__(self, coordinate_value, location):
        self.check_inputs(coordinate_value, location)
        self.value = coordinate_value
        self.set_location(location)
        self.set_initial_cant_be()
        self.solved = False
    
    def error_value_is_not_integer(self):
        error = "Non-integer value found. Please check your input and try "
        error += "again.\nSource: SudokuCoordinate"
        raise TypeError(error)
    
    def error_value_is_negative(self):
        error = "Negative value found. Please check your input and try again."
        error += "\nSource: SudokuCoordinate"
        raise ValueError(error)
        
    def error_value_is_greater_than_nine(self):
        error = "Value larger than 9 found. Please check your input and try "
        error += "again.\nSource: SudokuCoordinate"
        raise ValueError(error)
        
    def error_location_is_non_iterable(self):
        error = "Non-iterable location found. Please check your input to make"
        error += "sure all locations are of type 'tuple' or type 'list'.\n"
        error += "Source: SudokuCoordinate"
        raise TypeError(error)
        
    def error_location_is_too_long(self):
        error = "Location is not of length 2. Please check your input to make "
        error += "sure all locations are of length 2. Source: SudokuCoordinate"
        raise ValueError(error)
        
    def check_input_value(self, coordinate_value):
        if type(coordinate_value) != int:
            self.error_value_is_not_integer()
        elif coordinate_value < 0:
            self.error_value_is_negative()
        elif coordinate_value > 9:
            self.error_value_is_greater_than_nine()
            
    def check_if_in_range(self, axis_location):
        if axis_location < 0:
            self.error_value_is_negative()
        elif axis_location > 9:
            self.error_value_is_greater_than_nine()
            
    def check_if_integer(self, axis_location):
        if type(axis_location) != int:
            self.error_value_is_not_integer()
            
    def check_input_location(self, location):
        if type(location) != tuple and type(location) != list:
            self.error_location_is_non_iterable()
        if len(location) != 2:
            self.error_location_is_too_long()
        else:
            for axis_location in location:
                self.check_if_in_range(axis_location)
                self.check_if_integer(axis_location)
    
    def check_inputs(self, coordinate_value, location):
        self.check_input_value(coordinate_value)
        self.check_input_location(location)
        
    def set_location(self, location):
        if type(location) == list:
            self.location = tuple(location)
        else:
            self.location = location
            
    
    def set_initial_cant_be(self):
        if self.value:
            self.create_solved_cant_be()
        else:
            self.cant_be = [False]*9
    
    def get_cant_be_vector_count(self):
        counter = 0
        for value in self.cant_be:
            if value:
                counter += 1
        
        return counter
               
    def get_region_location(self):
        row = self.location[0]
        column = self.location[1]
        region_row_location = row%3
        region_column_location = column%3
        region_location = region_row_location*3 + region_column_location
        
        return region_location
        
    def create_solved_cant_be(self):
        self.cant_be = [True]*9
        self.cant_be[self.value -1] = False
    
    def get_mutual_allowables(self, shared_set, cant_be_index):
        """
        Finds all mutually allowed values between self and a shared set.
        Returns:
            - mutual_allowables: list, tuple, integers; list of the locations
            of all coordinates in the shared set that share allowable value
        """
        mutual_allowables = []
        for shared_set_index in range(9):
            if not shared_set[shared_set_index].cant_be[cant_be_index]:
                mutual_allowables.append(shared_set[shared_set_index].location)
        
        return mutual_allowables
    
    def single_exclusion(self, row, column, region):
        """
        Searches to see if there is any value, 1-9, for which this coordinate 
        is the only coordinate in its region, column, or row that can be that
        value.
        
        Inputs: 
            - row: Array, SudokuCoordinate(); the coordinates in the row that 
            this coordinate is a part of
            - column: Array, SudokuCoordinate(); the coordinates in the column 
            that this coordinate is a part of
            - region: Array, SudokuCoordinate(); the coordinates in the region
            that this coordinate is a part of
        """
        for cant_be_index in range(9):
            if not self.cant_be[cant_be_index]:
                for row_column_region_index in range(9):
                    mutual_row_allowables = self.get_mutual_allowables(row, cant_be_index)
                    mutual_column_allowables = self.get_mutual_allowables(column, cant_be_index)
                    mutual_region_allowables = self.get_mutual_allowables(region, cant_be_index)
                    if len(mutual_row_allowables) == 0:
                        self.value = cant_be_index + 1
                        self.create_solved_cant_be()
                        break
                    elif len(mutual_column_allowables) == 0:
                        self.value = cant_be_index + 1
                        self.create_solved_cant_be()
                        break
                    elif len(mutual_region_allowables) == 0:
                        self.value = cant_be_index + 1
                        self.create_solved_cant_be()
    
    def update_cant_be(self, row, column, region):
        """
        Inputs:
            - row: 1x9 Numpy Array; The full row that the coordinate is a member of
            - column: 9x1 Numpy Array; The full column that the coordinate is a member of
            - region: 3x3 Numpy Array; The region that the coordinate is a member of
        """
        for n in range(9):
        # If the cant_be property for this entry has not been determined yet
            # Check Row
            if row[n].value and n != self.location[1]:
                row_value = row[n].value
                self.cant_be[row_value - 1] = True
            # Check Column
            if column[n].value and n != self.location[0]:
                column_value = column[n].value
                self.cant_be[column_value - 1] = True
            # Check Region
            if region[n].value and n!= self.get_region_location():
                region_value = region[n].value
                self.cant_be[region_value - 1] = True
        # N-Exclusion
          
    def update_value(self):
        if self.get_cant_be_vector_count() == 8 and not self.value:
            for n in range(9):
                if self.cant_be[n] == False:
                    self.value = n+1
                    break
                