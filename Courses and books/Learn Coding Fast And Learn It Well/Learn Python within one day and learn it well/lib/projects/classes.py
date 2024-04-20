
#   Initiating object 'Game'
class Game():

    #   Initializing the Initializer
    def __init__(self, NOQ = 0):

        self._NOQ = NOQ

        return

    #   Declare a property 
    @property
    def NoQuestions(self):

        return self._NOQ

    @NoQuestions.setter
    def NoQuestions(self, value):

        #   If the value is less than 1
        if value < 1:

            #   add a initial value to the instance variable 
            self._NOQ +=1

            return print('Minimum Number of questions is 1')

        #   If the value is greater than 10
        elif value > 10:

            #   add a initial value to the instance variable 
            self._NOQ = 10

            return print('Maximum number of question is 10')

        else:

            self._NOQ = value

        return self._NOQ

#   Initiating object 'BinaryGame'
class BinaryGame(Game):

    #   Initializing the Initializer
    def __init__(self):
        return

    #   Generate questions method
    def GenerateQuestion(self):

        ''' 
                GenerateQuestions()
            an Instance method to generates binary questions.

        '''

        #   Importing randint function
        from random import randint

        #   Initializing a local variable called 'Score'
        Score   = 0

        #   Looping through using for loop to evaluate the answer
        for i in range(self._NOQ):

            #   Initializing a variable and choosing a random integer from 1-100
            x = randint(1,100)

            #   Prompt the user to type in an integer
            prmpt = input(f'Convert {x} into a binary:')

        #   Creating a while loop to loop through a true statement
        while True:

            #   Creating a try, except loop
            try:

                # Converting the string into an integer base 2
                prmpt = int(prmpt, base=2)

                if x == prmpt:

                #   Updating the user Score
                    Score += 1

                    print(f'Correct answer Score = {Score}')

                #   Breaking out from the while loop
                    break

                else:

                    print(f'The correct answer is {x} and you guessed {prmpt}')


            except ValueError as ve:

                #   Print out an error message
                print(ve
                )

            print('Game ended ', Score, ' points')
            prmpt = input(f'Convert {x} into a binary:')

            return Score

#   Initiating object 'MathGame'
class MathGame(Game):

    #   Initializing the Initializer
    def __init__(self, NOQ = 0):

        return