#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:22:43 2019

@author: Michael
"""

import unittest
from SudokuObjects import SudokuCoordinate

class InputsTestCase(unittest.TestCase):
    """
    Tests the __init__() method for the SudokuObjects.SudokuCoordinate class
    """
    
# Test the SudokuCoordinate.value attribute -----------------------------------
    
    def test_value_is_five(self):
        """
        Tests for when the value of the coordinate is an expected integer, 5
        """
        value = SudokuCoordinate(5,(0,0)).value
        self.assertEqual(5, value)
        
    def test_value_is_zero(self):
        """
        Tests for when the value of the coordinate is the expected minimum, 0
        """
        value = SudokuCoordinate(0, (0,0)).value
        self.assertEqual(0, value)
        
        
    def test_value_is_nine(self):
        """
        Tests for when the value of the coordinate is the expected maximum, 9
        """
        value = SudokuCoordinate(9, (0,0)).value
        self.assertEqual(9, value)
        
    def test_value_is_negative(self):
        """
        Tests for when the value of the coordinate is an unexpected negative 
        integer, -1
        """
        with self.assertRaises(ValueError):
            SudokuCoordinate(-1, (0,0))
         
    def test_value_is_10(self):
        """
        Tests for when the value of the coordinate is an unexpected large 
        integer, 10
        """
        with self.assertRaises(ValueError):
            SudokuCoordinate(10, (0,0))
            
    def test_value_is_a(self):
        """
        Tests for when the value of the coordinate is an unexpected character,
        'a'
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate('a', (0,0))
            
    def test_value_is_one_point_one(self):
        """
        Tests for when the value of the coordinate is an unexpected float,
        1.1
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(1.1, (0.0))
        
    def test_value_is_coordinate_object(self):
        """
        Tests for when the value of the coordinate is an unexpected object,
        SudokuCoordinate
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(SudokuCoordinate(0,(0,0)), (0,0))
  
# Test the SudokuCoordinate attribute -----------------------------------------
    def test_location_is_tuple_3_4(self):
        """
        Tests for when the location is an expected tuple, (3, 4)
        """
        location = SudokuCoordinate(0, (3,4)).location
        self.assertEqual((3,4), location)
    
    def test_location_is_list_3_4(self):
        """
        Tests for when the location is an expected list, [3, 4]
        """
        location = SudokuCoordinate(0, [3,4]).location
        self.assertEqual((3,4), location)
        
    def test_location_is_empty(self):
        """
        Tests for when the location is an unexpected empty tuple, ()
        """
        with self.assertRaises(ValueError):
            SudokuCoordinate(0, ())
            
    def test_location_is_large(self):
        """
        Tests for when the location is an unexpected large tuple, (0, 0, 0)
        """
        with self.assertRaises(ValueError):
            SudokuCoordinate(0, (0,0,0))
        
    def test_location_is_int(self):
        """
        Tests for when the location is an unexpected integer, 0
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(0, 0)
            
    def test_location_is_string(self):
        """
        Tests for when the location is an unexpected string, 'a'
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(0, 'a')
            
    def test_location_is_float(self):
        """
        Tests for when the location is an unexpected float, 1.1
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(0, 1.1)
            
    def test_location_is_object(self):
        """
        Tests for when the location is an unexpected object, SudokuCoordinate()
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(0, (0,0))
    
    
# Test the SudokuCoordinate.location[0] attribute -----------------------------
         
    def test_location_0_is_expected_integer(self):
        """
        Tests for when the location[0] is an expected integer, 3
        """
        location = SudokuCoordinate(0, (3,0)).location
        self.assertEqual((3,4), location)
        
    def test_location_0_is_min(self):
        """
        Tests for when the location is the expected minimum, (0,0)
        """
        location = SudokuCoordinate(0, (0,0)).location
        self.assertEqual((0,0), location)
    
    
    def test_location_0_is_max(self):
        """
        Tests for when the location is the expected maximum, (9,9)
        """
        location = SudokuCoordinate(0, (9,9)).location
        self.assertEqual((9,9), location)
        
    def test_location_0_contains_negative(self):
        """
        Tests for when the location contains a negative value
        """
        
    def test_location_0_contains_character(self):
        """
        Tests for when the location contains an unexpected character, a in 
        (a,9)
        """
        with self.assertRaises(TypeError):
            SudokuCoordinate(0, ('a',9))
        
        
        
unittest.main()