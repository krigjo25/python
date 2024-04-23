#   Importing responsories
import sys

from datetime import date, datetime

class MathFormulas():

    def __init__(self) -> None:
        pass

    #   Coleman-LiauFormula for Grading a reading
    def ColemanLiauFormula(self):

        '''
            #   Author :  krigjo25
            #   Date :    11.01-23

            #   The program should count the number of letters, words, and sentences in the text.
            #   -   You may assume that a letter is any lowercase character from `a-z, A-Z`
            #   -   Any sequence of characters separated by spaces should count as a word.
            #   -   Any occurrence of a `period`, `exclamation point`, or `question mark` indicates the end of a sentence.

            #   The program should print as output `Grade X`" where `X` is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.

            #   If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level) the program should output `Grade 16+` instead of giving the exact index number. 
            #   - If the index number is less than 1, your program should output "Before Grade 1".

            #   Coleman-Liau formula
            #   -   Average number of letters per 100 words
            #   -   Average numbers of sentence per 100 words
            #   -   L = letters / x words * 100
            #   -   S = sentence / x words * 100
            #   -   CLI = (L - S - 15.8)
            #   -   
        '''
        try:

            # Initializing variables
            arg = input("Calculate Sentence:")
            arg = str(arg).lower()

            w = self.CountingWord(arg)
            l = self.CountingLetters(arg)
            s = self.CountingSentences(arg)

            print(f"{l} Letters, {w} Words, {s} Sentences")

        except Exception as e: print(e)

        else:

            #   Calculating the Letters
            l = (l / w) * 100

            #   Calculating the Sentence
            s =  (s / w) * 100

            # Coleman Liau Formula
            cli = round((0.0588 * l) - (0.296 * s) - 15.8)

            print(f"{l} Letters, {w} Words, {s} Sentences, {cli} Grade")
            #   Checking if the condition is met
            if cli < 0: return print("Before Grade 1")
            elif cli > 15 : return print("Grade 16+")
            else : return print(f"Grade {cli}")

    def CountingWord(self, arg): return len(str(arg).split(" "))

    def CountingLetters(self, arg):

            l = ""

            for i in arg:
                if str(i).isalpha(): l += i

            return len(l)

    def CountingSentences(self, arg):

            # Initializing variables
            sentence = 0

            # Initializing arrays
            symbol = ["!", "?", "."]

            # Iterating through the argument
            for i in arg:

                # If the condition is met
                if i in symbol:
                    sentence += 1
            
            # Clean up
            del symbol

            return sentence

class MathCalculater():
    def __init__(self) -> None:
         pass

    def Calculatebmi(self, kg, cm, age, gender):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Creating a list of ASCII Decimal
            #   Checking if there is alphabetical letters in ASCIIdigits
            #   Formula for Caluclating Bmi
            #   -   Calculates bmi for adults and children

            #   -   Childrens 2-20
            #   -   kg / (m * m) * 10000

            #   -   Adults 20+
            #   -   kg / (m * m)
        '''

        #   Convert the height in meters
        m = cm / 100

        # Converts the weight into a integer
        kg = int(kg)
        
        #   Finds the bmi by dividing  with age and gender
        if age < 21 and gender == 'M':

            bmi = kg / (m * m) * 10000

        elif age < 21 and gender == 'F':

            bmi = kg / (m * m) * 10000

        else:
            bmi = kg / (m * m)

        return round(bmi, 2)

    def CalculateAge(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Calculates the age difference between the current
            #   -   date and the given date

            #   -   The leap year is added 
        '''

        try:

            #   Converting the date into a string, then back to a date
            prompt = str(input("Date of birth"))
            prompt = datetime.strptime(prompt, '%Y-%d-%m').date()

        except Exception as e: sys.exit(e)

        else:

            #   Get the today's date
            cur = date.today()

            #   Calculate the difference in years
            diff = cur - prompt.year  

        #   
        oneOrZero = ((cur.month, cur.day) < (prompt.month, prompt.day))

        #   fetching the age
        age = diff - oneOrZero

        #   Save space
        del cur
        del diff
        del prompt
        del oneOrZero

        return age
