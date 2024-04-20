
class Game():#   Initiating object 'Game'

    
    def __init__(self, NOQ = 0):#   Initializing the Initializer

        self._NOQ = NOQ

        return

    @property#   Declare a property 
    def NoQuestions(self): return self._NOQ

    @NoQuestions.setter
    def NoQuestions(self, value):

        if value < 1:#   If the value is less than 1
  
            self._NOQ +=1#   add a initial value to the instance variable 

            return print('Minimum Number of questions is 1')

        #   If the value is greater than 10
        elif value > 10:

            #   add a initial value to the instance variable 
            self._NOQ = 10

            return print('Maximum number of question is 10')

        else:

            self._NOQ = value

        return self._NOQ


class BinaryGame(Game):#   Initiating object 'BinaryGame'

    def __init__(self):#   Initializing the Initializer
        return

    #   Generate questions method
    def GenerateQuestion(self):

        ''' 
                GenerateQuestions()
            an Instance method to generates binary questions.

        '''

        from random import randint #   Importing randint function

        Score   = 0 #   Initializing a local variable called Score

        for i in range(self._NOQ):#   Looping through using for loop to evaluate the answer

            x = randint(1,100)#   Initializing a variable and choosing a random integer from 1-100

            #   Prompt the user to type in an integer
            prmpt = input(f'Convert {x} into a binary:')

        while True:# 

            try:

                prmpt = int(prmpt, base=2) # Converting the string into an integer base 2

                if x == prmpt:

                    Score += 1#   Updating the user Score

                    print(f'Correct answer Score = {Score}')

                #   Breaking out from the while loop
                    break

                else:

                    print(f'The correct answer is {x} and you guessed {prmpt}')

            except ValueError as e: print(e)#   Print out an error message

            print('Game ended ', Score, ' points')
            prmpt = input(f'Convert {x} into a binary:')

            return Score

class MathGame(Game):#   Initiating object 'MathGame'

    def __init__(self, NOQ = 0): #   Initializing the Initializer
        return