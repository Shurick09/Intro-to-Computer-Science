'''
Created on Feb 2, 2017

@author: Shurick
Alex Rozenblit
I pledge my honor that I have abided by the Stevens Honor System
'''

def dot(L,K):
    "Takes in two lists and returns their dot products"
    if L ==[] or K==[]:
        return 0
    return L[0]*K[0] + dot(L[1:],K[1:])

def explode(s):
    "Takes in a string and returns a list with each character of that string"
    if s=="":
        return []
    return [s[0]]+explode(s[1:])

def ind(e,L):
    "Looks for e in list or string L and returns the index where is e is first found. If not found return length of list or string L"
    if L==[] or L=="":
        0
    elif e !=L[0]:
        return ind(e,L[1:])+1
    return 0
        
     
def removeAll(e,L):
    "Removes all the e in list L"
    if L==[]:
        return []
    elif L[0]==e:
        return removeAll(e,L[1:])
    return [L[0]]+removeAll(e,L[1:])

def myFilter(f,L):
    "The filter functions returns a new list that contains all the elements of L for which the predicate returns True "
    if L==[]:
        return []
    elif f(L[0])== True:
        return [L[0]]+ myFilter(f,L[1:])
    return myFilter(f,L[1:])

def even(X):
    if X % 2 == 0 : return True     
    else: return False

def deepReverse(L):
    "Takes a list L and returns the reverse of that list"
    if L==[]:
        return []
    elif isinstance(L[-1],list):
        return [deepReverse(L[-1])]+deepReverse(L[:-1])
    return [L[-1]]+deepReverse(L[:-1])



print (dot([5,3],[6,4,10]))
print (explode("spam"))
print (ind(' ', 'outer exploration'))
print(removeAll(42,[55,[77,42],[11,42],88]))
print (myFilter(even, [0,1,2,3,4,5,6]))
print (deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))