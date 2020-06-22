'''
Created on Mar 28, 2017

@author: Shurick
'''

import random

def map_sqr(lst):
    result = []
    for x in lst:
        result.append(x * x)
    return result

def map_sqr2(lst):
    return [x * x for x in lst] #list comprehension

def average(lst):
    total = 0
    for x in lst:
        total = total + x
    return total / len(lst)

def find_max(L):
    if L == []:
        return None
    max_val = L[0]
    for x in L:
        if x > max_val:
            max_val = x
    return max_val

def find_min(L):
    if L == []:
        return None
    min_val = L[0]
    for x in L:
        if x < min_val:
            min_val = x
    return min_val

def find_min_max(L):
    if L == []:
        return None
    min_val = max_val = L[0]
    for x in L:
        if x > max_val:
            max_val = x
        elif x < min_val:
            min_val = x
    return (min_val, max_val)

def shallow_copy(L):
    '''Makes a shallow copy (1 level deep) of the elements in L and stores them in a new list.'''
    new_list = []
    for x in L:
        new_list.append(x)
    return new_list
    return[x for x in L]

def deep_copy(L):
    '''Makes a deep copy of a list, that is, copies lists within lists'''
    new_list = []
    for x in L:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

def sum_matrix(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total += matrix[row][col]
    return total
            
#S = [3, [1, 2], 9]
#T = shallow_copy(S)
#print(S)
#print(T)
#T[1][0] = 0
#print(S)
#print(T)

#S = [3, [1, 2], 9]
#T = deep_copy(S)
#print(S)
#print(T)
#T[1][0] = 0
#print(S)
    
grid = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)] 
#print(grid)
#print(sum_matrix(grid))

def print_grid(grid):
    for row in range(len(grid)):
        print(' ', end ='')
        for col in range(len(grid[row])):
            print(grid[row][col], end =' ')
            if col < 2:
                print('|', end=' ')
        print()
        if row < 2:
            print('-' * 11)
print(print_grid(grid))
        
    
print(map_sqr([25,1,4]))
print(map_sqr2([25,1,4]))
print(average([1,2,3,4]))
print(find_max([1,2,3,4,5]))
print(find_min([1,2,3,4,5]))
print(find_min_max([1,2,3,4,5]))