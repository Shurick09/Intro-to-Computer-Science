'''
Created on Feb 16, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System.
'''

def knapsack(capacity, itemList):
    '''
    knapsack takes in a capacity of the weight it can carry, and the itemList which contains the weight and value of all items
    that the person is considering stealing. The program computes what items to steal, so that the person can fit them in the
    knapsack and maximize value. The maximum value followed by the weight and value of each item stolen is returned.
    '''
    if capacity == 0:
        return [0,[]]
    elif itemList == []:
        return [0,[]]
    elif capacity < itemList[0][0]:
        return knapsack(capacity, itemList[1:])
    result = knapsack(capacity-itemList[0][0], itemList[1:])
    useIt = [result[0] + itemList[0][1] , [itemList[0]] + result[1]]
    loseIt = knapsack(capacity,itemList[1:])
    if useIt[0] < loseIt[0] :
        return loseIt
    return useIt



print(knapsack(6, [[1, 4], [5, 150], [4, 180]]))
print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]])) 
print(knapsack(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(25, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]])) 
print(knapsack(20, []))
print(knapsack(0, [[1, 1000], [2, 3000], [4, 55000]]))
print(knapsack(6, [[1, 4], [5, 150], [4, 180]]))

