'''
Created on Jan 27, 2017

@author: Shurick

Alex Rozenblit
I pledge my honor that I have abided by the Stevens Honor System.

'''
from cs115 import map, reduce, range
import math
from math import factorial

def inverse(n):
    "Will return reciprocal of n"
    return 1/n 


def e(n):
    "Approximates value of e with Taylor expansion."
    return sum(map(inverse,map(factorial,range(1,n+1))))+1

def error(n):
    "Absolute value of difference between actual e value and approximation"
    return abs(math.e-e(n))

