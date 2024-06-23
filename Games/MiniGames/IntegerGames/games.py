#   Importing Responsories
import sys
import random as r

#   Importing local libraries
from intgames.dict.gamedict import GameOver

class IntegerGames():

    '''
        #   Title   :       A Collection of Integer Games
        #   Author :        krigjo25
        #   Description :   
    '''

    def GameLevel(self, lvl):

        '''
            #   Choosing the difficulty level of the game
            #   The level has to be greater than 0
        '''

        while True:


            try :
                #   Ensure the input is an integer
                if not lvl.isdigit(): 
                    raise Exception("The level has to be an integer !")

                #   Ensure the input is greater than zero
                if lvl == None or int(lvl) < 1: 
                    raise ValueError("Choose an integer which is greater than zero")


            except (ValueError, Exception) as e: 
                print(e)

            return int(lvl)
            
    def GenerateIntegers(self, lvl):

        #   Ensure the lvl is one below
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
                return r.randint(500)


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
            n = self.GameFormula(lvl)
            #   Prompting the user for the output
            answer = input(f'{n[1]} = :')

            try :

                #   Ensure the variable contains an integer
                if not int(answer): raise ValueError("EEE")
                if int(answer) != n[0]: 
                    print('test')
                    raise Exception("EEE")

            except (ValueError, Exception) as e:

                #   Decrease lives by one
                print(e)
                lives -= 1

            if int(answer) == n[0]:

                #   Increasing the score
                lvl += 1
                score += 1
                

            #   Breaking out of the loop
            if lvl == 10: return print(f"Score : {score}\nLevels completed : {lvl}")
            if lives == 0: return print(f"Correct number : {n}\nScore : {score}\nLevels completed : {lvl}")


    def GuessTheNumber(self):

        #   Game Configurations
        lives= 3

        
        lvl = self.GameLevel()
        n = self.GenerateIntegers(lvl)

        while True:

            #   Prompting the user
            x = input('Guess: ')
            try :

                if x != n: raise Exception("EEE")
                if lives == 0: sys.exit(f"Number of levels won:{lvl}")
                if not int(x): raise ValueError("The inputted message must be an integer")

            except (ValueError, TypeError, Exception) as e: 
                
                lives -= 1
                print(e)

            #   Comparing the values

            if x == n: return print('Just right!')



if __name__ == '__main__':
    i = IntegerGames()
    i.LittleProffessor()
