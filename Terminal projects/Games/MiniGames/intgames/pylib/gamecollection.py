#   Importing Responsories
import sys
import random as r

from pylib.dict.game_over import GameOver

class IntegerGames():

    '''
        #   Title   :       A Collection of Integer Games
        #   Author :        krigjo25
        #   Description :   
                Creating a collection of Integer games
    '''
    def __init__(self):
        pass
    def GameLevel(self, lvl):

        '''
            #   Choosing the difficulty level of the game
            #   The level has to be greater than 0
        '''

        while True:


            try :
                #   Ensure the input is an integer
                if not str(lvl).isdigit() or lvl == None: 
                    raise ValueError("The level has to be an integer !")

                #   Ensure the input is greater than zero
                if int(lvl) < 1: 
                    raise ValueError("Choose an integer which is greater than zero")

            except ValueError as e: 
                sys.exit(f"USEAGE: In the terminal type intgame.py -h for commands.\n{e},")


            return int(lvl)
            
    def GenerateIntegers(self, lvl):

        #   Ensure the lvl is one of the below
        match lvl:
            case 1: 
                return [r.randint(0, 10), 'Guess a number between (1-10) :']

            case 2: 
                return [r.randint(0, 20), 'Guess a number between (1-20) :']

            case 3: 
                return [r.randint(0, 30), 'Guess a number between (1-30) :']

            case 4: 
                return [r.randint(0, 40), 'Guess a number between (1-40) :']

            case 5: 
                return [r.randint(0, 50), 'Guess a number between (1-50) :']

            case 6: 
                return [r.randint(0, 60), 'Guess a number between (1-60) :']
            
            case 7: 
                return [r.randint(0, 70), 'Guess a number between (1-70) :']
            
            case 8: 
                return [r.randint(0, 80), 'Guess a number between (1-80) :']
            
            case 9: 
                return [r.randint(0, 90), 'Guess a number between (1-90) :']
            
            case 10: 
                return [r.randint(0, 100), 'Guess a number between (1-100) :']
            case _:
                return [r.randint(0, 500), 'Guess a number between (1-500) :']

    def GameFormula(self, lvl):

        #   Generating integers
        x = self.GenerateIntegers(lvl)
        y = self.GenerateIntegers(lvl)

        match lvl:

            case 5:
                n = abs(x[0] - y[0])
                txt = f"{x[0]} - {y[0]}="
            
            case 6:
                n = abs(x[0] * y[0])
                txt = f"{x[0]} * {y[0]}="

            case _:
                n = abs(x[0] + y[0])
                txt = f"{x[0]} + {y[0]}="

        #   Initializing a list
        arg = []

        arg.append(n)
        arg.append(txt)

        #   Returning the 
        return arg

    def LittleProffessor(self): 

         #   Initializing Game Configurations
        lives = 3
        score = 0
        lvl = self.GameLevel(input('lvl :'))

        while True:

            #   Initializing the game
            print(f'Lives left : {lives}\tCurrent Score : {score}\t Current level: {lvl}')
            n = self.GameFormula(lvl)

            #   Prompting the user for the output
            answer = input(f'{n[1]} = :')

            try :

                #   Ensure the variable contains an integer
                if not int(answer): 
                    raise ValueError()

                if int(answer) != n[0]: 
                    raise Exception()

            except (ValueError, Exception) as e:

                #   Decrease lives by one
                print("EEE")
                lives -= 1

            if int(answer) == n[0]:

                #   Increasing the score
                lvl += 1
                score += 1
                print(f"Correct yay..")


            #   Breaking out of the loop
            if lvl == 10:
                
                return print(f"Score : {score}\nLevels completed : {lvl}")
            
            if lives == 0: 
                sys.exit(f"Correct number : {n}\nScore : {score}\nLevels completed : {lvl}")

    def GuessTheNumber(self):

        #   Game Configurations
        lives = 3
        lvl = self.GameLevel(input('lvl :'))
        n = self.GenerateIntegers(lvl)

        while True:

            #   Prompting the user
            answer = input(f'{n[1]} ')
            try :
                
                if int(answer) == n[0]: 

                    lvl += 1
                    lives += 1
                    print(f"""Congratz you won a new life
Current Stats:
Lifes : {lives} level: {lvl}""")
                    n = self.GenerateIntegers(lvl)
    
                else:
                    if n[0] > int(answer):
                        raise Exception('Too low, guess higher')
                    if n[0] < int(answer):
                        raise Exception('Too high, guess lower')

            except (ValueError, TypeError, Exception) as e: 
                
                lives -= 1
                print(e)


            if lives == 0: 
                    sys.exit(f"Number of levels won:{lvl}\n{GameOver().roundover(n,answer)}\n")

