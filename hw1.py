'''
Created on Jan 29, 2017

@author: Shurick

Alex Rozenblit
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import  map, reduce, range 

def mult(x,y):
    "Returns product of x and y"
    return x*y

def factorial(n):
    "Returns factorial of n"
    return reduce(mult,range(1,n+1))

def add(x,y):
    "Returns sum of x and y"
    return x+y

def mean(L):
    "Returns mean of list L"
    return reduce(add,L)/len(L)

def divides(n):
    "Finds out if n is divisible by k"
    def div(k):
        return n%k == 0
    return div

def prime(n):
    "Returns true if number is prime and false if it is composite"
    return sum(map(divides(n), range(1,n+1))) == 2
    
print (factorial(4))
print (mean([1,2,3,4]))
print(prime(5))
