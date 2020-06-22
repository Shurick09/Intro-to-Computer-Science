'''
Created on Jan 31, 2017

@author: Shurick
'''

from cs115 import reduce

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def tower(n):
    if n==0:
        return 1 
    return 2** tower(n-1)

def rTower(n):
    def power(x,y):
        return y**x
    return reduce(power, [2]*n)

def length(lst):
    if len(lst)==0:
        return 0
    return 1+ length(lst[1:])

def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
    
def powerSet(lst):
    if lst == []:
        return [[]]
    loseIt = powerSet(lst[1:])
    useIt = map(lambda x: [lst[0]] + x, loseIt)
    return loseIt + useIt

def subSet(target,lst):
    if target == 0:
        return True
    if lst == []:
        return False
    use_it = subSet(target-lst[0],lst[1:])
    lose_it = subSet(target,lst[1:])
    return use_it or lose_it

def subset_with_values(target,lst):
    if target == 0:
        return (True,[])
    if lst == []:
        return (False,[])
    use_it = subset_with_values(target-lst[0],lst[1:])
    if use_it[0]:
        return (use_it[0],[lst[0]]+use_it[1])
    return subset_with_values(target,lst[1:])
    #lose_it = subset_with_values(target,lst[1:])
    
def money(lst):
    if lst == []:
        return 0
    useIt = lst[0] + money(lst[2:])
    loseIt = money(lst[1:])
    return max(useIt,loseIt)

def money_values(lst):
    if lst == []:
        return (0,[])
    useIt = money_values(lst[2:])
    newSum = lst[0] + useIt[0]
    loseIt = money_values(lst[1:])
    if newSum > loseIt[0] :
        return(newSum, [lst[0]] + useIt[1])
    return loseIt

def LCS_with_values(s1,s2):
    if s1 == '' or s2 == '':
        return (0, '')
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:],s2[1:])
        return (1+result[0]), s1[0] + result[1]
    useS1 = LCS_with_values(s1,s2[1:])
    useS2 = LCS_with_values(s1[1:],s2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

def distance(first,second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:],second[1:])
    substitution = 1 + distance(first[1:],second[1:])
    deletion = 1 + distance(first[1:],second)
    insertion = 1 + distance(first,second[1:])
    return min(substitution, deletion, insertion)

def pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pell(n-1) + 2 * n + pell(n-1)


#print(distance('extradoinaary','applemelon'))
print (factorial(4))
print(tower(4))
print (rTower(4))
print (length([3,4,5,6,6]))
print (fib(5))
print (subSet(50,[4,6,9,25,12]))
print (subset_with_values(50,[4,6,9,25,12]))
print (money([5,10,1,2]))
print (money_values([5,10,1,2]))
print (LCS_with_values('pi','pi'))
print (distance('spot','sata'))
print(pell(0))
print(pell(4))