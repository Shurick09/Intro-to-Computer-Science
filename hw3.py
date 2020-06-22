'''
Created on Feb 14, 2017

@author: Shurick

Alex Rozenblit

I pledge that I have abided by the Stevens Honor System.
'''
from cs115 import map

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount,coins):
    "Returns the minimum number of coins needed to make amount, followed by a list of those coins"
    if amount == 0:
        return [0,[]]
    elif coins == []:
        return [float("inf"),[]]
    elif amount < coins[0]:
        return giveChange(amount,coins[1:])
    useIt = giveChange(amount-coins[0], coins)
    newSum= 1 + useIt[0]
    loseIt = giveChange(amount, coins[1:])
    if newSum < loseIt[0]:
        return [newSum, [coins[0]]+useIt[1]]
    return loseIt

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter,scorelist):
    "Returns the value of a specfic letter"
    if(scorelist == []):
        return None
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter,scorelist[1:])

def wordScore(s,scorelist):
    "Returns the value of an entire word"
    if s == '':
        return 0
    return letterScore(s[0],scorelist) + wordScore(s[1:],scorelist)



def wordsWithScore(dct,scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, Dictionary) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    
    return map(lambda word: [word,wordScore(word,scores)],dct)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0:
        return []
    return [L[0]] + take(n-1,L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n==0:
        return []
    return drop(n-1,L[:-1]) + [L[-1]]
    

print(giveChange(35, [1, 3, 16, 30, 50]))
print(wordsWithScore(Dictionary, scrabbleScores))
print(take(3,[1,2,3,4,5,6]))
print(drop(3,[1,2,3,4,5,6]))