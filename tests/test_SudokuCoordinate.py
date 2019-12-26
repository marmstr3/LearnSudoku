#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:22:43 2019

@author: Michael
"""

import unittest
from SudokuObjects import SudokuCoordinate

class InitTestCase(unittest.TestCase):
    """
    Tests the __init__() method for the SudokuObjects.SudokuCoordinate class
    """
    
    def test_value_is_five(self):
        """
        Tests for when the value of the coordinate is an expected integer, 5
        """
        value = SudokuCoordinate(5,(0,0)).value
        self.assertEqual(5, value)
        
        
unittest.main()