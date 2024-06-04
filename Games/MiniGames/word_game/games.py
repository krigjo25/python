#   Importing Responsories
import os
import sys
import random as r
import time as t

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
            prompt = str(prompt.content).lower()

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

    def madlibsStory(self):

        #   Initializing variable and the library list
        madlibs = ""
        madlibslist = ["the photographer", "butterfly"]

        #   Iterating through the list, and assignt values into a string
        for i in madlibslist: madlibs += f"{i.capitalize()}, "

        #   Checking if there is a story to type
        while True:

            try:

                #   Prompting the user for a message
                prompt = input(f"Choose a story between : {madlibs} :").lower()

                #   Returns false, returns only true if prompt = None, why?
                if prompt not in madlibslist : raise TypeError(" Story does not exist, contact the maintainer to fix it.")

                for i in prompt:
                    if str(i).isdigit(): raise ValueError("The title of story does not contain numbers")
            except Exception as e: print(e)
            else:
                print(f"You've choosen {prompt.capitalize()}.\ninput atlast two words in the following inputs.")
                break

        while True:

            try:

                #   Story inputs
                adjectives = input("Adjectives for the story? (seperate with \",\" comma): ").split(",")
                color = input("Colours for the story? (seperate with \",\" comma):").split(",")
                things = input("Things for the story? (seperate with \",\" comma)").split(",")
                location = input("Locations for the story? (seperate with \",\" comma)").split(",")
                person = input("Names of people of the story : (seperate with \",\" comma)").split(",")
                animals = input("Names of animals / insects of the story (seperate with \",\" comma)").split(",")
                verbs = input("Verbs for the story? (seperate with \",\" comma)").split(",")
                food = input("food products for the story? (seperate with \",\" comma)").split(",")
                clothes = input("clothes for the story? (seperate with \",\" comma)").split(",")
                profession = input("professions for the story? (seperate with \",\" comma)").split(",")

                #   Initializing a 2D array
                words = [adjectives, color, things, location, person, animals, verbs, food, profession]

                for i in words:

                    #   1D Lists¨
                    if len(i) < 2:

                        #   Error messages based on index
                        match words.index(i):

                            case 0: raise ValueError("There has to be more than 1 adjective")
                            case 1: raise ValueError("There has to be more than 1 color")
                            case 2: raise ValueError("There has to be more than 1 thing")
                            case 3: raise ValueError("There has to be more than 1 location")
                            case 4: raise ValueError("There has to be more than 1 person")
                            case 5: raise ValueError("There has to be more than 1 animal")
                            case 6: raise ValueError("There has to be more than 1 verb")
                            case 7: raise ValueError("There has to be more than 1 food product")
                            case 8: raise ValueError("There has to be more than 1 proffesion")
                            case 9: raise ValueError("There has to be more than 1 cloth")

                    for j in i:
                        for k in j:

                            if str(k).isdigit(): raise ValueError("The string can not contain any numbers.")

                #   Clear some space
                del words

                #   Terminate the while loop
                break
    
            except Exception as e : print(e)

        #   Initializing variable
        madlibs = ""

        match prompt:

            case "the photographer":

                #   Creating strings
                string = f"Say {food[r.randrange(0,len(food))]}, The Photographer said as the camera flashed!"
                string1 = f"{person[r.randrange(0,len(person))]} and I had gone to {location[r.randrange(0,len(location))]} to get our photos taken on my birthday."
                string2 = f"The first photo we really wanted was a picture of us dressed as {animals[r.randrange(0,len(animals))]}, pretending to be a {profession[r.randrange(0,len(profession))]}."
                string3 = "When we saw the second photo, it was exactly what I wanted."
                string4 = f"We both looked like {things[r.randrange(0,len(things))]} wearing {clothes[r.randrange(0,len(clothes))]} and {verbs[r.randrange(0,len(verbs))]} -- that were exctly what i had in mind."

                #   Print output
                print(string, string1, string2, string3, string4)

                #   Clear some space
                del string3, string4

            case "butterfly":

                #   Creating strings
                string = f"Last night I dreamed I was a {adjectives[r.randrange(0,len(adjectives))]} butterfly with {color[r.randrange(0,len(color))]} splocthes that looked like {things}."
                string1 = f"I flew to {location[r.randrange(0,len(location))]} with my bestfriend and {person[r.randrange(0,len(person))]} who was a {adjectives[r.randrange(0,len(adjectives))]} {animals[r.randrange(0,len(animals))]}."
                string2 = f"We ate some {food[r.randrange(0,len(food))]} when we got there and then decided to {verbs[r.randrange(0,len(verbs))]} and the dream ended when I said-- lets {verbs[r.randrange(0,len(verbs))]}."

                #   Print output
                print(string, string1, string2)

                # clear some space

        #   Clear some memory
        del string, string1, string2
        del adjectives, color
        del things, location
        del animals, verbs
        del food, profession
        del prompt, madlibslist

        return

if __name__ == "__main__":
    wordgames = WordGames()
    wordgames.madlibsStory()