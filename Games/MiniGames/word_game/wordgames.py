#   Importing Responsories
import os
import sys
import random as r
import time as t

from pylib.command_line_tool import CommandlineInterface
from dotenv import load_dotenv


from pylib.databasePython import MariaDB
from dictionary.gamedicitonary import Philosopher, JumbleCategory, GameOver, ReactionGame, ScrabbleGame, APITools, Madlibs

load_dotenv()

class WordGames():

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic WordGames
    '''

    def __init__(self): pass

    #   Game Configurations
    def GameLevel(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Checking if the prompted integer is less than 1

        '''

        #   Declare a list
        count = []

        while True:

            try :



                #   Wait for an answer and handling the string
                lvl = int(input("Game Configurations\nType in a level"))

                if lvl < 1: raise ValueError('The level can not be less than one')

            except Exception as e : print(type(e))

            else:

                lvl = int(lvl)

                #   Configuring the timer based on level
                if lvl < 10: sec = 60.0
                elif lvl > 9 and lvl < 20: sec = 50.0
                elif lvl > 19 and lvl < 30: sec = 40.0
                elif lvl > 29 and lvl < 40: sec = 30.0
                elif lvl > 39 and lvl < 50: sec = 20.0
                else: sec = 15.0

                return sec

    def JumbleGame(self):


        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Welcome the user to the game & Prompting for category
            #   Promting for a sub category
            #   Randomizing the dictionary word
            #   Request a solve
            #   Creating a new word with joining the elements of the iterator

        '''

        #   Initializing the classes

        jumble = JumbleCategory()

        #   Configure the jumble Settings
        word = []
        sub = ""
        category = ""
        lvl = self.GameLevel()

        category = [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]

        for i in category: sub += f"{i}, ".capitalize()

        while True:

            print(f'Please select one of the categories below:\n\n{sub}')
            del sub

            #   Prepare and retrieve the category
            prompt = input("Select one of the categories below :")
            prompt = str(prompt).lower()

            try :

                if len(prompt) < 2: raise ValueError("Category has to contain more than one character")
                if prompt not in category: raise ValueError("Category does not exist")

            except Exception as e: print(e)

            else: break
        

        if prompt in category[0]: answer = APITools().NinjaChoice()
        else:

            try :

                #   Fetch sub categories from database
                category = MariaDB(database=os.getenv("database")).SelectRow("categories", prompt )

            except Exception as e: print(e)

            else:

                sub = ""

                #   Iterate through the categories and add category to variable
                for i in category[2:]: sub += f"{i}, "

                print(f"Selected category {category[1]}\n{sub}")
                prompt = input("Type in a category:")

                #   Fetching the answer from the database
                answer = MariaDB(database=os.getenv("database")).SelectColumn(category[1], "roles", prompt, "characters")
                answer = answer[r.randrange(0, len(answer))]
                #   Randomizing the answer       
                

            #   Clear some space
            del category, sub
            del prompt

        while True:

            #   Declear a string variable
            string = ""
        
            virvel = jumble.JumbleGenerator(answer)

            try :

                #   Prompting the user for a word
                prompt = input(f"Guess the jumbled word (q to quit): \"{virvel}\"")

            except Exception as e:print(e)

            else:

                word.append(prompt)

                match prompt:

                    case "q":

                        for i in word: string += f"**{i}**,"

                        #   GameOver message
                        print(f"Game Summary\nWords tried : ({string})\n\nThe correct answer : {answer}")

                        break

                    case answer:

                        for i in word: string += f"{i} "

                        print(f'words tried : ( {string} )\nCounted {len(word)} attempts.\n{GameOver().CorrectAnswer()}')

                        break

            tempt -1
            if tempt == 0:

                print(f"Game Summary\nWords tried : ({string})\n\nThe correct answer : {answer}")

                break

        #   Save space and clear fields
        #del tmpt
        del word, string
        del virvel, prompt
        del answer

        return

    def EightBall(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompt the user for an answerAsk a question with what, how or why
            #   Combine the answers
            #   Send a philliosofically answer

        '''

        #   Initializing array
        arr = ['what', 'how', 'why',]

        #   Print an output
        print("Ask the Philiosopher a question")

        #   Initialize a string
        quiz = ""

        #   Prompting the user for a question
        prompt = input("Question :" ).split(" ")

        try :

            for i in prompt:
                quiz += f"{i} "
                for j in i:
                    #   if the condition is met raise
                    if str(j).isdigit() : raise ValueError('Numeric inputs is not valid.')

        except Exception as e : sys.exit(e)

        else:

            #   Checking for certain words in prompted message.
            if "how" in prompt[0] or "what" in prompt[0] : prompt = Philosopher().Answer()
            else: prompt = Philosopher().DumbFacts() 

            #   Prepare and send the embed
            print(f"Answer for {quiz}\n{prompt}")

         #   Clear fields and save space

        del arr
        del quiz
        del prompt

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

                #   Wait for an answer and handling the string
                word = [input("Player one :"), input("Player two :")]

                for i in word:
                    if bool(ScrabbleGame().NinjaCheck(i)) == False:  raise ValueError(f'"{i}" Is not a word')

            except (ValueError, TypeError) as e: print("An error occured\n {e}\n Try again...")

            else:

                score = [ScrabbleGame().ComputeScore(word[0]), ScrabbleGame().ComputeScore(word[1])]

                #  Checking whom Scored Highest
                if score[0] > score[1]: print("Player 1 is the winner")
                elif score[0] < score[1]: print("Player 2 is the winner")
                else:
                    print(f"Game over\n {GameOver().TowTie()}")
                    break

        #   Save some space
        del i
        del lvl
        del word
        del score

        return

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
    WordGames().main()