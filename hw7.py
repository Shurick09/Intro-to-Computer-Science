'''
Created on Mar 22, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System
'''

FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def numToBaseB(n,b):
    ''' Turns number n in decimal to the same number in base b '''
    if b > n:
        return n
    elif n == 0:
        return '0'
    else:
        return numToBaseBHelper(n,b)

def numToBaseBHelper(n,b):
    ''' Main code for numToBaseB. Helper function needed because of specific base case problem '''
    if n== 0:
        return ''
    elif n % b == 0:
        return numToBaseBHelper(n/b,b) + '0'
    else:
        return numToBaseBHelper(n//b,b) + '1'

def baseBToNum(s,b):
    ''' Turns s in base b to its equivalent in decimal'''
    def baseBToNumHelper(s,b,counter):
        if s == '':
            return '0'
        elif b == 10:
            return s
        elif int(s[-1]) == 1:
            counter = counter + 1
            return int(baseBToNumHelper(s[:-1],b,counter)) + b**counter
        else:
            counter = counter + 1
            return baseBToNumHelper(s[:-1],b,counter)
    return baseBToNumHelper(s,b,-1)

def baseToBase(b1,b2,sinb1):
    '''Turns sinb1 from base b1 to base b2 '''
    return numToBaseB(int(baseBToNum(sinb1,b1)),b2)

def add(s,t):
    ''' Adds s and t by converting both into base 10 and then converting back to base 2'''
    return numToBaseB(baseBToNum(s,2) + baseBToNum(t,2),2)

def addB(x,y):
    '''Adds binary numbers without having to convert them to decimal'''
    def addBHelper(x,y,carryBit):
        if len(x) != len(y):
            return eqlen(x,y)
        elif len(x) == 0 and carryBit == '1':
            return '1'
        elif len(x) == 0:
            return ''
        else:
            sumBit, carryBit = FullAdder[(x[-1],y[-1],carryBit)]
            return addBHelper(x[:-1],y[:-1],carryBit) + sumBit
    return addBHelper(x,y,'0')
             
def eqlen(x,y):
    ''' Ensures that addB will work even if the two numbers inputed are'nt the same lengths '''
    if len(x) > len(y):
        return addB(x,(len(x) - len(y)) * '0' + y)
    else:
        return addB((len(x) - len(y)) * '0' + x,y)
    
print(numToBaseB(4,2))
print(numToBaseB(4, 3))
print(numToBaseB(34, 6))
print(numToBaseB(0, 4))
print(baseBToNum("11", 2))
print(baseBToNum("11", 3))
print(baseBToNum("", 10))
print(baseToBase(2, 10, "11"))
print(baseBToNum('3',10))
print(baseToBase(10, 2, "3"))
print(baseToBase(3, 5, "11"))
print(add("11", "01"))
print(add("011", "100"))
print(add("110", "011"))
print(addB("11", "1"))
print(addB("011", "100"))