'''
Created on Apr 18, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''

DAYS_OF_THE_WEEK = {0:'Tuesday', 1:'Wednesday', 2:'Thursday', 3:'Friday', 4:'Saturday', 5:'Sunday', 6:'Monday'}

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
    
    def tomorrow(self):
        '''Changes self to the day after self'''
        if self.isLeapYear() == True:
            DAYS_IN_MONTH = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day != DAYS_IN_MONTH[self.month]:
            self.day = self.day + 1
        elif self.month != 12 and self.day == DAYS_IN_MONTH[self.month]:
            self.day = 1
            self.month = self.month + 1
        else: 
            self.day = 1
            self. month = 1
            self.year = self.year + 1
    
    def yesterday(self):
        '''Changes self to the day before self'''
        if self.isLeapYear() == True:
            DAYS_IN_MONTH = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day != 1:
            self.day = self.day - 1
        elif self.day == 1 and self.month != 1:
            self.day = DAYS_IN_MONTH[self.month - 1]
            self.month = self.month -1
        else:
            self.day = 31
            self.month = 12
            self.year = self.year - 1
    
    def addNDays(self,N):
        '''Prints everyday up to N days after self'''
        for i in range(N+1):
            print(self)
            self.tomorrow()
        self.yesterday()

    def subNDays(self,N):
        '''Prints everyday up to N days before self'''
        for i in range(N+1):
            print(self)
            self.yesterday()
        self.tomorrow()
        
    def isBefore(self,d2):
        '''Returns True if the calling object is a calendar date before the input d2 and False otherwise'''
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        else:
            if self.month < d2.month:
                return True
            elif self.month > d2.month:
                return False
            else:
                if self.day < d2.day:
                    return True
                elif self.day > d2.day:
                    return False
                else:
                    return False 
                
    def isAfter(self,d2):
        '''Returns True if the calling object is a calendar date after the input d2 and False otherwise'''
        if self.equals(d2):
            return False
        else:
            return not self.isBefore(d2)
    
    def diff(self,d2):
        '''Returns an integer representing the number of days between self and d2'''
        day1 = self.copy()
        day2 = d2.copy()
        c = 0
        if self.equals(d2):
            return 0
        elif self.isBefore(d2):
            while day1.isBefore(day2):
                day1.tomorrow()
                c = c + 1
            return c * -1 
        else:
            while day1.isAfter(d2):
                day1.yesterday()
                c = c + 1
            return c
    
    def dow(self):
        '''Returns the day of the week at which Date is on'''
        d2 = Date(4,18,2017)
        return DAYS_OF_THE_WEEK[self.diff(d2) % 7]
