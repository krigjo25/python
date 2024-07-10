#   Importing responsories
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, ArgumentError


class CommandlineInterface():

    '''
        The command line Interface
    '''
    version = "0.0.1"
    author = "Krigjo25"
    name = "wg"
    description = "Collection of Word Games"

    def CommandLineOptions(self):

        '''Constructing the argparser'''
        #   Initializing the parser
        parser  = ArgumentParser(prog = self.name, formatter_class= ArgumentDefaultsHelpFormatter, description= self.description, epilog= f"Thanks for using this v{self.version} of %(prog)s")
        
        #   Initializing parser groups
        faq = parser.add_argument_group('How to')
        games = parser.add_argument_group('Available Games')
        
        #   Initializing The helper interface
        games.add_argument('-j', dest = 'jumble', help ='The Jumble Game', action='store_true')
        games.add_argument('-e', dest = 'eight', help ='EightBall Game', action='store_true')
        games.add_argument('-s', dest = 'scrabble', help ='Scrabble Game', action='store_true')
        games.add_argument('-i', dest = 'info', help = '%(prog)s info Center', action='store_true')
        games.add_argument('-c', dest = 'credits', help = '%(prog)s Credential Center', action='store_true')
        games.add_argument('-r', dest = 'rsp', help ='Rock Scissors and paper Game (Emoji game)', action='store_true')

        #   Game Guide
        faq.add_argument('-f--rsp', dest = 'faq_rps', help ='How to use Rock Scissors\'n Paper', action='store_true')
        faq.add_argument('-f--jumble', dest = 'faq_jumble', help ='How to use Jumble', action='store_true')
        faq.add_argument('-f--Scrabble', dest = 'faq_scrabble', help ='How to use Scrabble', action='store_true')
        faq.add_argument('-f--eightball', dest = 'fag_eightball', help ='How to use Eightball', action='store_true')

        #   Initializing the parser
        cmd = parser.parse_args(sys.argv[1:])
        
        try :

            if not cmd:
                raise Exception("Command not found")

        except (ArgumentError, Exception) as e: 
            sys.exit(e)

        return cmd
    
    def Porgaminfo(self):
        return sys.exit(f"\n\nProgram name : {self.name}\nVersion : {self.version}\nDescription : {self.description}\n")

    def ProgramCredits(self): 
        return sys.exit("""
            Libraries used in the project :
            
            requests  - by Kenneth Reitz
            os, sys -  by
            dotenv -   by 
            pytest - pytest - by pytest team
            sys - Python built-in responsories
            random - Python built-in responsories
            argparse - Python command line tool responsories

            Project © Created by : @krigjo25
        """)
 
    def faqrps(self):
        
        return sys.exit(
            """ 
            Frequently Asked Questions : Rock, Scissors and paper
            USEAGE : python wordgames.py -rsp\n
            1. Type in either Rock, Scissors or Paper
            The bot then will randomly choose Rock, Scissors or paper, then print out a message.\n
        """)
    def faqjumble(self):
        return sys.exit(""" 
            Frequently Asked Questions : Jumble
            USEAGE : python wordgames.py -j\n
            1.\n
        """)

    def faqeightball(self):

        return sys.exit(""" 
            Frequently Asked Questions : Eightball
            USEAGE : python wordgames.py -e\n
            1. Type in a sentence and the eightball will reply\n
        """)

    def faqscrabble(self):
        """ 
            Frequently Asked Questions : Scrabble
            USEAGE : python wordgames.py -s\n
            1. Type in how many human will play
            2.  Type in how many bots will play
            3. Select name for the human players
            4. Every participants types in a word
            5. wait for the program to calculate\n
           
        """
        return sys.exit()