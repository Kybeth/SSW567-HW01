"""
Author: Yuan Zhang
Course: SSW 567
Description of this script: HW01 - Testing triangle classification
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    try:
        int(a)
        int(b)
        int(c)
    except ValueError:
        return 'Not numbers!'
    a,b,c= tuple(sorted(tuple((a,b,c)))) # Sort the three sides
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c:
        return 'Isoceles'
    elif a^2 + b^2 == c^2:
        return 'Right'
    elif a + b <= c:
        return 'NotATriangle'
    else:
        return 'Scalene'
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


class TestTriangles(unittest.TestCase):
    def testSet1(self): # test invalid inputs
        self.assertEqual(classifyTriangle('the', 'wandering','earth'), 'Not numbers!')
        self.assertEqual(classifyTriangle('1o', 8, 6), 'Not numbers!')
        
    def testMyTestSet2(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','10,10,10 should be Equilateral')
        self.assertNotEqual(classifyTriangle(10,15,30),'Scalene','10,15,30 should be NotATriangle')
        self.assertNotEqual(classifyTriangle(1,2,1), 'Isoceles','1,2,1 should be NotATriangle') # This line finds a bug in the 
        self.assertEqual(classifyTriangle(10,6,8), 'Right', '10,6,8 should be Right')
        self.assertEqual(classifyTriangle(10,10,1), 'Isoceles', '10,10,1 should be Isoceles')

        
if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    