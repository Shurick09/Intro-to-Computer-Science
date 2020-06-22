'''
Created on Feb 5, 2017

@author: Shurick

CS115 - HW2

Alex Rozenblit

I pledge that I have abided by the Stevens Honor System
'''


import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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

def count(letter,L):
    "Returns the amount of the letter in list or string L "
    if L == "" or L == []:
        return 0
    elif letter == L[0]:
        return count(letter,L[1:])+1
    return count(letter,L[1:])
    
def canSpell(rack,word):
    "Determines if the rack of letters can be used to spell word"
    if word == "":
        return True
    elif count(word[0],word) > count(word[0],rack):
        return False
    return canSpell(rack,word[1:])
    
def scoreList(rack):
    "Returns every word in the Dictionary that can be spelled with the letters in rack followed by the score of that word"
    lst=(filter(lambda word: canSpell(rack,word),Dictionary))
    return map(lambda word:[word,wordScore(word,scrabbleScores)],lst)

def maxPair(a,b):
    "Compares 2 sets of [word,score of word]. Returns the set with the greater score of word. "
    if a[1]>b[1]:
        return a
    return b

def bestWord(rack):
    "Returns the word with the highest score that can be made the letters in rack, followed by that word's score"
    if scoreList(rack)==[]:
        return ["",0]
    return reduce(maxPair,scoreList(rack))



print(letterScore("b", scrabbleScores))
print(wordScore("wow", [['o', 10], ['w', 42]]))
print (count('a',['a','b','c','a','a','a']))
print (scoreList(["a", "s", "m", "t", "p"]))
print (bestWord(['g', 'y', 'e']))