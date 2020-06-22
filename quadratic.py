'''
Created on Apr 19, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System.
'''

class QuadraticEquation(object):
    '''Defines an object which is a quadratic equation'''
    
    def __init__(self,a,b,c):
        '''Constructs a quadratic equation'''
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    
    def discriminant(self):
        '''Returns the discriminant of the quadratic equation'''
        return (self.b ** 2) - (4 * self.a * self.c)
    
    def root1(self):
        '''Computes one root of the quadratic equation when the sign is +'''
        if self.discriminant() < 0:
            return None
        else:
            return (((-1 * self.b) + (((self.b ** 2) - (4 * self.a * self.c))) ** 0.5)) / (2 * self.a)
    
    def root2(self):
        '''Computes one root of the quadratic equation when the sign is -'''
        if self.discriminant() < 0:
            return None
        else:
            return (((-1 * self.b) - (((self.b ** 2) - (4 * self.a * self.c))) ** 0.5)) / (2 * self.a)
        
    def __str__(self):
        '''Returns a string representation of the quadratic equation'''
        a = str(self.a) + 'x^2 '
        b = '+ ' + str(self.b) + 'x '
        c = '+ ' + str(self.c) + ' = 0'
        if self.a == -1:
            a = '-x^2 '
        elif self.a == 1:
            a = 'x^2 '
        if self.b == -1:
            b = '- x '
        elif self.b == 1:
            b = '+ x '
        elif self.b == 0:
            b = ''
        elif self.b < 0:
            b = '- ' + str(abs(self.b)) + 'x '
        if self.c < 0:
            c = '- ' + str(abs(self.c)) + ' = 0'
        elif self.c == 0:
            c = '= 0'
        return a + b + c
            