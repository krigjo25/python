#   Importing Responsories
import sys
import random as r

from os import getenv
from dotenv import load_dotenv

#   Importing local libraries
from Games.MiniGames.IntegerGames.dict.gamedict import GameOver
from Games.MiniGames.IntegerGames.pylib.mariadb import MariaDB

load_dotenv()

class IntegerGames():

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic WordGames
    '''

    def GameLevel(self):

        '''
            #   Choosing the difficulty level of the game
            #   The level has to be greater than 0
        '''

        while True:

            try :
                lvl = int(input('level : '))
                if not str(lvl).isdigit(): raise Exception('The level has to be an integer greater than 0')
                if lvl == None or lvl < 1 : raise ValueError('Choose an integer grater than 0')


            except (ValueError,) as e: print(e)

            return lvl
            
    def GenerateIntegers(self, lvl):

        match lvl:
            case 1: return r.randint(0, 10)
            case 2: return r.randint(0,20)
            case 3: return r.randint(0,30)
            case 4: return r.randint(0,40)
            case 5: return r.randint(0,50)
            case 6: return r.randint(0,60)
            case 7: return r.randint(0,70)
            case 8: return r.randint(0,80)
            case 9: return r.randint(0,90)
            case 10: return r.randint(0,100)


        return

    def Operators(self, lvl):

        dictionary = {  1:'+',
                        #2:'-',
                        #3:'/',
                        #4:'*',
                        }

        r.shuffle(dictionary)

        arg = []
        rint = r.randint(1, len(dictionary))

        x = self.GenerateIntegers(lvl)
        y = self.GenerateIntegers(lvl)

        if dictionary[rint] == '+':

            n = x + y
            mf = f"{x} + {y} = "

        arg.append(n)
        arg.append(mf)
        print(mf)
        print(n)
        #   Returning the 
        return arg

    #   Games
    def LittleProffessor(self):

        #   Game Configurations
        #   Prompting a level input
        lvl = self.GameLevel()

        #   Calculating the answer
        arg = self.Operators(lvl)

        #   Initializing variables
        score = 0
        etempt = 3

        while True:

            try :
                #   Prompting the user for the output
                prmpt = int(input(f"{arg[1]}"))

            except ValueError as e:

                #   Decrease the score by one
                etempt -= 1
                print('EEE')
                if etempt == 0: return print(f'Correct number : {arg[0]} \n Score : {score}')

            else:

                if prmpt == arg[0]:

                    #   Adding one point to score
                    score += 1

                    #   Creating a new math problem to be solved
                    x = r.randint(0,10)
                    y = r.randrange(0,10)

                    #   Calculating the answer
                    arg = self.Operators(lvl)


                elif prmpt != arg[0]:

                    print('EEE')
                    etempt -= 1
                    arg = self.Operators(lvl)

                #   Breaking out of the loop
                if etempt <= 0: return print(f'Correct number : {arg[0]} \n Score : {score}/9')
                elif score == 9: return print(f'Score : {score}')

    def GuessTheNumber(self):

        #   Initializing variables
        tempt = 3

        #   Game Configurations
        lvl = self.GameLevel()
        n = self.GenerateIntegers(lvl)

        while True:

            
            try :
                #   Prompting the user
                x = int(input('Guess: '))

            except (ValueError, TypeError) as e: continue

            else:
                #   Comparing the values

                if x == n: return print('Just right!')
                else: print(GameOver().intGame())

                #   End game
                if tempt == 0: return print(GameOver.IncorrectAnswer())

if __name__ == '__main__':
    i = IntegerGames()
    i.LittleProffessor()
