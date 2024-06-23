#   Importing Responsories
import os
import sys
import time as t
import random as r

from dotenv import load_dotenv


from pylib.databasePython import MariaDB
from dictionary.gamedicitonary import Philosopher, JumbleCategory, GameOver, ReactionGame, ScrabbleGame, APITools, Madlibs
from pylib.command_line_tool import CommandlineInterface

load_dotenv()


class WordGames():

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic WordGames
    '''

    def __init__(self): pass

    #   Game Configurations
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

    def JumbleGame(self):

        #   Initializing the classes

        jumble = JumbleCategory()

        #   Configure the jumble Settings
        word = []
        
        sub = ""
        lives = 3
        lvl = self.GameLevel(input('Choose a level:'))


        for i in [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]: 
            sub += f"{i}, ".capitalize()



        while True:

            print(f"Please select one of the categories below:\n\n{sub}")
            
            #   Prepare and retrieve the category
            prompt = input("category:")
            prompt = str(prompt).lower()

            try :

                if len(prompt) < 2: 
                    raise ValueError("Category has to contain more than one character")

                if prompt not in [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]: 
                    raise ValueError("Category does not exits")

            except ValueError as e: 
                print(e)

        

            if prompt in category[0]: 
                answer = APITools().NinjaChoice()
            else:

                try :

                    #   Fetch sub categories from database
                    category = MariaDB(database=os.getenv("database")).SelectRow("categories", prompt )

                except Exception as e: 

                    print(e)

                sub = ""

                #   Iterate through the categories and add category to variable
                for i in category[2:]:
                    sub += f"{i}, "

                print(f"Selected category {category[1]}\n{sub}")
                
                prompt = input("Type in a category:")

                #   Fetching the answer from the database
                answer = MariaDB(database=os.getenv("database")).SelectColumn(category[1], "roles", prompt, "characters")

                #   Randomizing the answer
                answer = answer[r.randrange(0, len(answer))]      
                

            #   Clear memories
            del category, sub
            del prompt

            #   Declear a string variable
            string = ""
        
            #   The confusing answer
            virvel = jumble.JumbleGenerator(answer)

            #   Prompting the user for a word
            prompt = input(f"Guess the jumbled word (q to quit): \"{virvel}\"")

            try :
                 if lives == 0: raise Exception()
                 elif "q" in prompt: raise Exception("User Quit") 

            except Exception as e:

                print(e)
                sys.exit(f"Game Summary\nWords tried : ({string})\n\nThe correct answer : {answer}")
                

            word.append(prompt)

            if prompt == answer:

                for i in word: 
                    string += f"{i} "

                print(f'words tried : ( {string} )\nCounted {len(word)} attempts.\n{GameOver().CorrectAnswer()}')

            
           

            #   #   Clear some memories
            del word, string
            del virvel, prompt
            del answer, lives

    def EightBall(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompt the user for an answerAsk a question with what, how or why
            #   Combine the answers
            #   Send a philliosofically answer

        '''

        #   Initializing array

        #   Print an output
        print("Ask the Philiosopher a question")

        #   Initialize a string
        quiz = ""

        #   Prompting the user for a question
        prompt = input("Question :" ).split(" ")

        try :

            for i in prompt:
                quiz += f"{i} "

            #   Ensure the condition is met
            if str(prompt).isdigit():
                raise ValueError('Numeric inputs is not valid.')

        except Exception as e :
            sys.exit(e)

        #   Ensure that prompt is in arr
        if prompt[0] in ['what', 'how']: 
            prompt = Philosopher().Answer()

        else:

            prompt = Philosopher().DumbFacts() 

        print(f"Answer for {quiz}\n{prompt}")

         #  Clear memories
        del quiz, prompt

        return

    def Scrabble(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompts the words for each player
            #   Calculating the score for both words
            #   Printing the winner

            #   Player required : 1 - 2

        '''
        #   Initializing lists
        word = []

        lvl = self.GameLevel()

        while True:

            try:

                #   Prompts the words for both players
                print(f'Available dictionaries : :england:, :flag_us:')

                #   Wait for an answer before handling the string
                word = [input("Player one :"), input("Player two :")]

                for i in word:

                    if bool(ScrabbleGame().NinjaCheck(i)) == False:  
                        raise ValueError(f'"{i}" Is not a word')

            except (ValueError, TypeError) as e: 
                print("An error occured\n {e}\n Try again...")

            else:

                score = [ScrabbleGame().ComputeScore(word[0]), ScrabbleGame().ComputeScore(word[1])]

                #   Clear memories
                del i, lvl, word

                #   Ensure the the player whom has the highest score
                if score[0] > score[1]: 
                    return print("Player 1 is the winner")

                elif score[0] < score[1]:
                    return print("Player 2 is the winner")

                else:

                    return print(f"Game over\n {GameOver().TowTie()}")


    def RockScissorPaper(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompt the user for a string
            #   Combine the answers
            #   Send a philliosofically answer

        '''

        #   Initializing classes
        rsp = ReactionGame()

        #   Initializing an array with Rock, Scissors, Paper
        arr = [ "rock", "scissors", "paper"]



        #   Game Configuration
        #lvl = self.GameLevel()

        try :

            prompt = str(input("Rock, Scissors or Paper : ")).lower()

            #   Error messages
            if prompt not in arr: raise ValueError("Choose between Rock, Scissors or paper")
            elif prompt.isalpha() : pass
            else: raise ValueError("Prompted message contains digits, it can only contain alpha()")

        except Exception as e : print(e)

        else:

            dictionary = {
                        "rock": "\U0001FAA8",
                        "scissors": "\U00002702",
                        "paper": "\U0001F4C4"
            }

            prompt = dictionary.get(prompt)
            #   Computer chooses between one of Rock, Scissors and paper
            x = rsp.RockScissorPaper()
            print(x, prompt)

            #   Check for winner and print out output
            if prompt == x: print(GameOver().TowTie())

            else:

                #   If the user win
                if prompt == '\U0001F4C4' and x =='\U0001FAA8': print(f" {rsp.Player(prompt,x)}")
                if prompt == '\U0001FAA8' and x =='\U00002702': print(f" {rsp.Player(prompt,x)}")
                if prompt == '\U00002702' and x =='\U0001F4C4': print(f" {rsp.Player(prompt,x)}")

                 #   if the bot wins
                if x == '\U0001F4C4' and prompt =='\U0001FAA8': print(f"{rsp.Computer(x)}")
                if x == '\U0001FAA8' and prompt =='\U00002702': print(f"{rsp.Computer(x)}")
                if x == '\U00002702' and prompt =='\U0001F4C4': print(f"{rsp.Computer(x)}")

                #   Clear fields
                del x
                del rsp
                del arr
                del prompt
                
                return


    def main(self): 
        
        """
            Command-line tool to interact with the games
        """

        cmd = CommandlineInterface()

        if cmd.CommandLineOptions().credits: 
            return cmd.ProgramCredits()
            
        elif cmd.CommandLineOptions().info: 
            return cmd.Porgaminfo()
        
        elif cmd.CommandLineOptions().rsp: 
            return self.RockScissorPaper()

        elif cmd.CommandLineOptions().scrabble: 
            return self.Scrabble()
        
        elif cmd.CommandLineOptions().eight: 
            return self.EightBall()
        
        elif cmd.CommandLineOptions().jumble: 
            return self.JumbleGame()

if __name__ == "__main__":
    WordGames().JumbleGame()