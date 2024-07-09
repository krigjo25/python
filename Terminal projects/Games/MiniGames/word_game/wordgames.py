#   Importing Responsories
import os
import sys
import random as r

from dotenv import load_dotenv

from pylib.apis import NinjaAPI
from pylib.databasePython import MariaDB
from dictionary.gamedicitonary import Philosopher, JumbleCategory, GameOver, ReactionGame, ScrabbleGame
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
                answer = NinjaAPI().Choice()
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
            #   Description :
                prompts the user to type in a question,
    

            #   Prompt the user for an answerAsk a question with what, how or why
            #   Combine the answers
            #   Send a philliosofically answer

        '''
        arr = ['what', 'how']

        #   Print an output
        print("Ask the Philiosopher a question")

        #   Prompting the user for a question
        prompt = str(input("Question :" ))
        quiz = prompt

        prompt = prompt.split(" ")

        
        #   Ensure that prompt is in arr
        if prompt[0].lower() in arr: 
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

        while True:

            try:

                #   Prompts the words for both players
                print(f"Welcome to the Scrabble Game terminal version !")
                print(f'Available dictionaries : :england:, :flag_us:')
                print(f"How to play : First we will ask for your name\n then just type in a word to collect points.")
                print(f"However if the word is false, no points is collected otherwise each letter has a point.")

                name = [input("Player one's name: "), input("Player two's name: ")]
                
                #   Wait for an answer before handling the string
                word = [input(f"{name[0]}: "), input(f"{name[1]}: ")]

                for i in word:

                    if bool(ScrabbleGame().CheckWord(i)) == False:  
                        raise ValueError(f'"{i}" Is not a word')

            except (ValueError, TypeError) as e: 
                print("An error occured\n {e}\n Try again...")

            score = [ScrabbleGame().ComputeScore(word[0]), ScrabbleGame().ComputeScore(word[1])]

            #   Clear memories
            del i, word

            #   Ensure the the player whom has the highest score
            if score[0] > score[1]:
                return print(f"Scoreboard:\n{name[0]} has {score[0]}points\n {name[1]} has {score[1]}points\n{name[0]} won ! congratulations")

            elif score[0] < score[1]:
                return print(f"Scoreboard:\n{name[0]} has {score[0]}points\n{name[1]} has {score[1]}points\n{name[1]} won ! congratulations")

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

        prompt = str(input("Rock, Scissors or Paper : ")).lower()

        try :

            #   Error messages
            if prompt not in arr: 
                raise ValueError("Choose between Rock, Scissors or paper")

            elif prompt.isdigit():
                raise ValueError("Prompted message contains digits, it can only contain alpha()")

        except Exception as e : 
            sys.exit(e)

        else:

            dictionary = {
                        "rock": "\U0001FAA8",
                        "scissors": "\U00002702",
                        "paper": "\U0001F4C4"}

            prompt = dictionary.get(prompt)

            #   Computer chooses between one of Rock, Scissors and paper
            x = rsp.RockScissorPaper()

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

        try :
            if len(sys.argv) < 2: raise Exception("Usage : python wordgames.py -h or --help to view the command list")

        except Exception as e:
            sys.exit(e)

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