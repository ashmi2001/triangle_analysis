# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import os
from triangle import classify_triangle
  # Import the xmlrunner to generate XML output

# Your existing TestTriangle class should be here
# For example:
# class TestTriangle(unittest.TestCase):
#     ...

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles', '2,2,3 should be an Isosceles triangle')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classify_triangle(5, 5, 3), 'Isosceles', '5,5,3 should be an Isosceles triangle')

    # Test Scalene Triangle
    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(6, 7, 8), 'Scalene', '6,7,8 should be a Scalene triangle')

    # Test for invalid triangles
    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1,10,12 should not be a valid triangle')

    # Test for invalid inputs (out of range, zeros, negative numbers)
    def testInvalidInputA(self): 
        self.assertEqual(classify_triangle(201, 10, 10), 'InvalidInput', '201,10,10 should be an Invalid Input')

    def testInvalidInputB(self): 
        self.assertEqual(classify_triangle(0, 10, 10), 'InvalidInput', '0,10,10 should be an Invalid Input')

    def testInvalidInputC(self): 
        self.assertEqual(classify_triangle(-1, 10, 10), 'InvalidInput', '-1,10,10 should be an Invalid Input')

    def testInvalidInputD(self): 
        self.assertEqual(classify_triangle(10, "a", 10), 'InvalidInput', '10,"a",10 should be an Invalid Input')

    # Edge case: four inputs
    def testFourInputs(self):
        with self.assertRaises(TypeError):  # Expecting TypeError if extra arguments are passed
            classify_triangle(1, 1, 1, 1)

    # Edge case: imaginary numbers
    def testImaginaryNumbers(self):
        self.assertEqual(classify_triangle(3+4j, 3+4j, 3+4j), 'InvalidInput', 'Imaginary numbers should be Invalid Input')

    # Edge case: string inputs
    def testStringInputs(self):
        self.assertEqual(classify_triangle('a', 'b', 'c'), 'InvalidInput', 'String inputs should be Invalid Input')

    # Edge case: mixed invalid types
    def testMixedInputs(self):
        self.assertEqual(classify_triangle(10, 20, 'c'), 'InvalidInput', 'Mixed valid and invalid inputs should be Invalid Input')

if __name__ == '__main__':
    print('Running unit tests')
    
    # Create the test-results directory if it doesn't exist
    os.makedirs('test-results', exist_ok=True)
    
    # Run the tests and generate results.xml in the test-results directory
    with open('test-results/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), verbosity=2)


