'''
Created on Jan 26, 2017

@author: Shurick
'''

from cs115 import map, reduce, range
def span(lst):
    return reduce(max,lst)-reduce(min,lst)

print (span([2,3,4,5,6,8]))

def gauss(N):
    range(1,N+1)