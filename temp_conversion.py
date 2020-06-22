'''
Created on Jan 24, 2017

@author: Shurick
'''
def fahrenheit(celsius):
    """ Returns the input celsius degrees in fahrenheit. """
    return 9/5 * celsius + 32

def celsius(fahrenheit):
    """ Returns the input fahrenehit degrees in celsius. """
    return 5/9 * (fahrenheit -32)

c=float(input ("Enter degrees in Celsius"))
f=fahrenheit(c)

print(c, 'C =', f, 'F')
print('%.2f C = %.2f F' %(c,f))

f=float(input("Enter degrees in Fahrenheit"))
c= celsius(f)
print(f, 'F=', c, 'C')
assert print(fahrenheit(celsius(f))) == f