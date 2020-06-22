'''
Created on Feb 21, 2017

@author: Shurick

Alex Rozenblit

I pledge that I have abided by the Stevens Honor System.
'''
'''
def pascal_row(x):
    if x == 0:
        return [1]
    if pascal_row(x-1)[1:] == []:
        return [1]
    return [1] + [pascal_row(x-1)[0] + pascal_row(x-1)[1]] + pascal_row(x-1)[1:]
    
    Why doesn't it work when I write it this way?
'''

def pascal_row(x):
    "Returns a specific row in Pascal's Triangle"
    if x == 0:
        return [1]
    return [1] + row(pascal_row (x - 1))

def row(y):
    "Uses the rows above the desired row to find the desired row. This function adds adjacent elements in the list representing the"
    "above rows to find the desired row."
    if y[1:] == []:
        return [1] 
    return [y[0] + y[1]] + row(y[1:])

def pascal_triangle(n):
    "Returns all the rows from 0 to n in Pascal's triangle"
    return map(lambda x: pascal_row(x),range(0,n+1))


print (pascal_row(0))
print (pascal_row(1))
print (pascal_row(2))
print (pascal_row(3))
print (pascal_row(4))
print (list(pascal_triangle(6)))