'''
Created on Feb 28, 2017

@author: Shurick

CS115 - Hw 5

Alex Rozenblit

I pledge my honor that I have abided by the Stevens honor system.
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.
"""
def sv_tree(trunk_length, levels):
     Takes in a trunk length and amount of branches out and draws a tree using the built in turtle python feature.
    if levels == 1:
        turtle.forward(trunk_length)
        turtle.backward(trunk_length)
        return       
    else:
        turtle.forward(trunk_length)       
        turtle.left(45)         
        sv_tree(trunk_length/2, levels-1)     
        turtle.right(90)         
        sv_tree( trunk_length/2 , levels-1)      
        turtle.left(45)       
        turtle.backward(trunk_length)     

"""
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''

    def lucas_helper(n, memo):
        if n in memo:
            return memo[n]
        elif n == 0:
            result = 2
        elif n == 1:
            result = 1 
        else:
            result = lucas_helper(n-1,memo) + lucas_helper(n-2,memo) 
        memo[n] = result
        return result
    return lucas_helper(n,{})


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[amount,coins]
        elif amount == 0:
            result = 0
        elif coins == ():
            result = float("inf")
        elif amount<coins[0]:
            result = fast_change_helper(amount,coins[1:], memo)
        else:
            useIt = fast_change_helper(amount-coins[0],coins, memo) + 1
            loseIt = fast_change_helper(amount,coins[1:], memo)
            result = min(useIt,loseIt)
        memo[amount,coins] = result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
#sv_tree(128,6)