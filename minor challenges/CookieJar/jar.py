'''
    Title : Bank
    Description :   A program that prompts user for owned cash

    Base by : CS50 Problem set 09 Introduction to Python
    Developed by : @krigjo25
    Date Started : 25.11-23
    Date Submited : 24.11-23
    Date re-Submited : N/A

        #   __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar.
        #   If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
        #   __str__ Returns a str  🍪, multiplied by capacity
        #   If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
        #   Withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
        #   Capacity should return the cookie jar’s capacity.
        #   Counter should return the number of cookies actually in the cookie jar.
        #   Structure your class per the below.
        #   You may not alter these methods’ parameters, but you may add your own methods.
'''
class Jar:

    def __init__(self, capacity = 12):

        self._cookie = ''
        self.__capacity = capacity

        if self.__capacity < 1: raise ValueError('Capacity can not be less than 1')

        return


    def __str__(self):
        return f'{self._cookie}'

    def deposit(self, x):

        #   Does not raise valueError
        if  x > self.__capacity or x < 1 or len(self._cookie) > self.__capacity: raise ValueError(f'Can only deposit between 1-{self.__capacity} cookie(s)')
        else: self._cookie += x * '🍪'

        return self._cookie


    def withdraw(self, x):


        if x > len(self._cookie) or x > self.__capacity or x < 0: raise ValueError('Can not withdraw that much cookies')
        else:
            x -= len(self._cookie)
            self._cookie = x * '🍪'

        return self._cookie

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self,x):

        '''
            #   Rules for how to use the capacity attribute
            #   Raising valueError if the capacity is less than 1

        '''
        try :
            if self.__capacity < 1: raise ValueError()

        except ValueError as e:
            print(e)

        self.__capacity = x
        return self.__capacity

    @property
    def size(self):
        return self._cookie

    @size.setter
    def size(self, x):

        '''
            #   Rules for cookies

            #   Raising ValueError if there is less than zero cookies left
        '''
        try:
            #   Ensure the cookie is not in the variable
            if '🍪' not in x: self._cookie = 'zero cookies'

            #   Ensure  there is cookies left
            else: self._cookie = x
        except ValueError as e:
        return self._cookie
