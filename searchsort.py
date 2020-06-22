'''
Created on Apr 10, 2017

@author: Shurick
'''

import random
import time

def sequential_search(lst,key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binary_search(lst,key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -low - 1

'''
print(binary_search(lst,1))
print(binary_search(lst,-1))
print(sequential_search([1,2,3,4,5], 3))


lst = [1,2,3,5,7,9,10,11]
key = -1
index = binary_search(lst, key)
if index >= 0:
    print('Key %d found at index %d' %(key, index))
else:
    print('Key %d not found, but can be inserted at index %d.' % (key, -index-1))

'''
lst = [random.randint(1,100000) for _ in range(500000)]
lst.sort()
start = time.clock()
sequential_search(lst, 200000)
elapsed = (time.clock() - start) * 1000

print('Seq %0.3f ms' % elapsed)

start = time.clock()
binary_search(lst, 200000)
elapsed = (time.clock() - start) * 1000

print('Bin %0.3f ms' % elapsed)