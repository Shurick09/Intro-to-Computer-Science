'''
Created on Feb 10, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System
'''
 
def change(amount, coins):
    "Takes in an amount of change as well as various different valued coins. Returns the the fewest amount of coins needed to make that amount."
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    elif amount<coins[0]:
        return change(amount,coins[1:])
    useIt = change(amount-coins[0],coins) + 1
    loseIt = change(amount,coins[1:])
    return min(useIt,loseIt)
    
    
print(change(48, [1, 5, 10, 25, 50]))
print(change(48, [1, 7, 24, 42]))
print(change(35, [1, 3, 16, 30, 50]))
print(change(131, [1, 5, 10, 20, 50, 100]))
print(change(292, [1, 5, 10, 20, 50, 100]))
print(change(673, [1, 5, 10, 20, 50, 100]))
print(change(724, [1, 5, 10, 20, 50, 100]))
print(change(888, [1, 5, 10, 20, 50, 100]))


