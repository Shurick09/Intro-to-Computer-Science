''''
Created on Apr 5, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System.
'''

import random, sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A = A + [createOneRow(width)]    # What do you need to add a whole row here?
    return A

def printBoard(A):
    """ this function prints the 2d list-of-lists
     A without spaces (using sys.stdout.write) """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells. """  
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):    
            if row == col:        
                A[row][col] = 1            
            else:                
                A[row][col] = 0          
    return A

def innerCells(w,h):
    ''' creates a board with all 1's except for
     the outside border which will be all 0's  '''
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):    
            A[row][col] = 1        
    return A

def randomCells(w,h):
    ''' creates a board with randomly assigned 0's or 1's
    except for the outer edge which is all 0's '''
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):    
            A[row][col] = random.choice([0,1])        
    return A

def copy(A):
    ''' creates a deep copy of array A'''
    x = createBoard(len(A[0]),len(A))
    for row in range(len(A[0])):
        for col in range(len(A)):
            x[row][col] = A[row][col]
    return x

def innerReverse(A):
    ''' reverses each elemen in array A except 
    the outer edges which are kept at 0'''
    x = createBoard(len(A[0]),len(A))
    for row in range(1,len(A[0])-1):
        for col in range(1,len(A)-1):
            if A[row][col] == 0:
                x[row][col] = 1
            else:
                x[row][col] = 0
    return x
        
def next_life_generation(A):
    """ makes a copy of A and then advanced one 
    generation of Conway's game of life within 
    the *inner cells* of that copy.
    The outer edge always stays 0."""
    newA = copy(A)
    for row in range(1,len(A[0])-1):
        for col in range(1,len(A)-1):
            if countNeighbors(row,col,A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row,col,A) > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and countNeighbors(row,col,A) ==3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA
            

def countNeighbors(row,col,A):
    ''' counts the amount neighbors A[row][col] has '''
    x = 0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if A[r][c] == 1:
                x = x + 1
    if A[row][col] == 1:
        return x-1
    else:
        return x

A = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
print(printBoard(A))
A2 = next_life_generation(A)
print(printBoard(A2))
print(countNeighbors(2,2,A))
A3 = next_life_generation(A2)
print(printBoard(A3))
print(createOneRow(3))
print(createBoard(3, 4))