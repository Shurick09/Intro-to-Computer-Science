'''
Created on Feb 16, 2017

@author: Shurick
'''

import turtle 

def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(distance+initial* (count%2), initial, count+1)
    square_spiral_helper(20, 20, 0)
    
square_spiral(100)