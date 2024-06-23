#   Importing Responsories
import sys
import random as r

from pylib.command_line_tool import CommandlineInterface
from pylib.dict.game_over import GameOver

class IntegerGames():

    '''
        #   Title   :       A Collection of Integer Games
        #   Author :        krigjo25
        #   Description :   
                Creating a collection of Integer games
    '''

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
                return r.randint(0, 10)

            case 2: 
                return r.randint(0,20)

            case 3: 
                return r.randint(0,30)

            case 4: 
                return r.randint(0,40)

            case 5: 
                return r.randint(0,50)

            case 6: 
                return r.randint(0,60)
            
            case 7: 
                return r.randint(0,70)
            
            case 8: 
                return r.randint(0,80)
            
            case 9: 
                return r.randint(0,90)
            
            case 10: 
                return r.randint(0,100)
            case _:
                return r.randint(0,500)

    def GameFormula(self, lvl):

        #   Generating integers
        x = self.GenerateIntegers(lvl)
        y = self.GenerateIntegers(lvl)

        match lvl:

            case 5:

                n = abs(x - y)
                txt = f"{x} - {y} = "
            
            case 6:

                n = abs(x * y)
                txt = f"{x} * {y} = "

            case _:
                n = abs(x + y)
                txt = f"{x} + {y} = "

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
                print(f"{GameOver().roundover(n,answer)}\n")
                

            #   Breaking out of the loop
            if lvl == 10:
                
                return print(f"Score : {score}\nLevels completed : {lvl}")
            
            if lives == 0: 
                sys.exit(f"Correct number : {n}\nScore : {score}\nLevels completed : {lvl}")

    def GuessTheNumber(self):

        #   Game Configurations
        lives = 3
        lvl = self.GameLevel(lvl)
        n = self.GenerateIntegers(lvl)

        while True:

            #   Prompting the user
            answer = input('Guess: ')
            try :

                if answer != n: 
                    raise Exception()

            except (ValueError, TypeError, Exception) as e: 
                
                lives -= 1
                print(print(f"{GameOver().roundover(n,answer)}\n"))

            #   Comparing the values

            if answer == n: 
                return print(f"{GameOver().roundover(n,answer)}\n")

            if lives == 0: 
                    sys.exit(f"Number of levels won:{lvl}\n{GameOver().roundover(n,answer)}\n")

    def main(self):

        cmd = CommandlineInterface()

        if cmd.CommandLineOptions().credits: 
            return cmd.ProgramCredits()
            
        elif cmd.CommandLineOptions().info: 
            return cmd.Porgaminfo()
        
        elif cmd.CommandLineOptions().tlp: 
            return self.LittleProffessor()

        elif cmd.CommandLineOptions().gtn: 
            return self.GuessTheNumber()

if __name__ == '__main__':
    IntegerGames().main()
