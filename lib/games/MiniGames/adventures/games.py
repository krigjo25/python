#   Importing Responsories
import sys
import random as r

from os import getenv
from dotenv import load_dotenv

#   Importing local libraries
from dictionary.stories import Folklore, Stories
from pylib.databasePython import MariaDB

load_dotenv()

class AdventureGames():

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic WordGames
    '''

    #   Game Configurations
    def GameSettings(self, lvl):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Checking if the prompted integer is less than 1

        '''

        try :

            if lvl < 1: raise ValueError('The level can not be less than one')

        except Exception as e : print(type(e))

        else:

            match lvl:

                case 1: count = 10
                case 5: count = 7
                case 10: count = 3

        return count

    #   Database connection
    def DatabaseConnection(self, database ,table,  arg):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Connecting to the Database
            #   Creating a new word with joining the elements of the iterator

        '''
        #   Initializing variables & classes
        db = MariaDB()
        database = database

        #   Selecting from table
        query = f'SELECT {arg} FROM {table}'
        word = db.selectFromTable(database, query)

        #   Closing the connection
        db.closeConnection()

        #   Clean up
        del db
        del query
        del database

        return word

    def MadLabGenerator(self):

        print("Seperate words with comma")

        madlab = [Folklore(), Stories()]

        while True:
            try:

                #   Prompting the user for some inputs
                names = str(input("Input some names:")).split(",")
                color = str(input("Input some colours: ")).split(",")
                prompt = str(input("Input some adjectives :")).split(",")
                

                #   Rasing value errors
                for i,j in prompt,:
                    if i.isdigit(): raise ValueError('The string can not contain any numbers')
                    elif not i.isalpha() : raise ValueError('The string can not contain any special characters')

                    if j.isdigit(): raise ValueError('The string can not contain any numbers')
                    elif not j.isalpha() : raise ValueError('The string can not contain any special characters')


            except Exception as e : print(e)
            else:
                arg = madlab.Generator(prompt, color)
    
            return

    def DungeonGenerator(self): pass

if __name__ == '__main__':
    w = AdventureGames()