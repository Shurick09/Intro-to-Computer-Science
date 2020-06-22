'''
Created on Mar 2, 2017

@author: Shurick

Alex Rozenblit

CS115 - Lab 6

I pledge my honor that I have abided by the Stevens Honor System.

'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return (n%2 != 0)

""" 42 - 32 = 10 (Left-most digit 1), 10 - 16 = -6 (No good, next digit is 0), 10 - 8 = 2 (Next digit is 1),
2 - 4 = -2 (No good, the next digit is 0), 2 - 2 = 0 (Next digit is 1, Since equals 0, fill in 0's for the rest of powers of 2,
Only one 0 needed),  42_10 = 101010_2 """

""" An odd base-10 number as well as an odd base-2 number will both have a 1 for the right-most bit.
An even base-10 number as well as an odd base-2 number will both have a 0 for the right-most bit."""
  
""" By eliminating the right-most digit in a base 2 number, the number is being divided by 2 and then truncated to 0 decimal places"""

""" If we had the base-2 representation of Y we will only have to add one digit on the right-hand side of the number.
If N is even we will need to add a 0 on the right-hand side Y to make it equal N.
If N is odd we will need to add a 1 at the right-hand side of Y to make it equal N."""


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n/2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNum_helper(s,c):
        if s == '':
            return 0
        else:
            return binaryToNum_helper(s[:-1],c+1) + int(s[-1])* 2**c
    return binaryToNum_helper(s,0)

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ((8-len(numToBinary(binaryToNum(s)+1))) * '0') + numToBinary(binaryToNum(s)+1)[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n != -1:
        print(s)
        count(increment(s),n-1)
    return ''

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n%3 != 0:
        return numToTernary(n//3) + str(n%3)
    else:
        return numToTernary(n//3) + '0'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def ternaryToNum_helper(s,c):
        if s == '':
            return 0
        else:
            return ternaryToNum_helper(s[:-1],c+1) + int(s[-1]) * 3**c 
    return ternaryToNum_helper(s,0)



print(isOdd(5))
print(isOdd(4))
print(numToBinary(15))
print(numToBinary(1))
print(binaryToNum('1010'))
print(binaryToNum(''))
print(binaryToNum('0'))
print(increment('00000000'))
print(increment('00000111'))
print(increment('11111111'))
print(count("00000000", 4))
print(numToTernary(42))
print(ternaryToNum('1120'))