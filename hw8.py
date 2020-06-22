'''
Created on Mar 28, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System.
'''

def TcToNum(x):
    ''' Returns the integer that x is the two's compliment of'''
    if x[0] == '0':
        return binaryToNum(x)
    else:
        return int(binaryToNum(toggler(minus_one(x)))) * -1

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

def minus_one(x):
    ''' Subtracts one from x'''
    if x[-1] == '1':
        return x[:-1] + '0'
    else:
        return minus_one(x[:-1]) + '1'

def toggler(x):
    ''' Returns the x with its digits toggled'''
    if x == '':
        return ''
    elif x[0] == '0':
        return '1' + toggler(x[1:])
    else:
        return '0' + toggler(x[1:])

def NumToTc(x):
    '''Returns the two's complement of x '''
    if x > 127 or x < -128:
        return 'Error'
    elif x >= 0:
        return ((8 - len(numToBinary(x))) * '0') + numToBinary(x)
    else:
        return  add_one(toggler((((8 - len(numToBinary(x * -1))) * '0') + numToBinary(x * -1))))

def add_one(x):
    ''' Adds one to x'''
    if x == '':
        return '1'
    elif x[-1] == '0':
        return x[:-1] + '1'
    else:
        return add_one(x[:-1]) + '0'
    
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

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return (n%2 != 0)

print(TcToNum('00000001'))
print(TcToNum("11111111"))
print(TcToNum("10000000"))
print(TcToNum("01000000"))
print(TcToNum("01111111"))
print(NumToTc(1))
print(NumToTc(-50))
print(NumToTc(-128))
print(NumToTc(200))
print(NumToTc(-127))
print(numToBinary(127))