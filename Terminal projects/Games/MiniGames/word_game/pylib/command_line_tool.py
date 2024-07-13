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
        parser  = ArgumentParser(prog = self.name, formatter_class=ArgumentDefaultsHelpFormatter, description= self.description, epilog= f"Thanks for using this v{self.version} of %(prog)s")
        
        #   Initializing parser groups

        games = parser.add_argument_group('Available Games')
        guide = parser.add_subparsers(title = 'How To', help='Game Guides')
        
        
        #   Initializing The helper interface
        games.add_argument('-j', dest = 'jumbleGame', help ='The Jumble Game', action='store_true')
        games.add_argument('-e', dest = 'eightballGame', help ='EightBall Game', action='store_true')
        games.add_argument('-s', dest = 'scrabbleGame', help ='Scrabble Game', action='store_true')
        games.add_argument('-rsp', dest = 'rspGame', help ='Rock Scissors and paper Game (Emoji game)', action='store_true')

        #   Game Guides
        faq = guide.add_parser( 'faq', help="USEAGE: -f -h")
        faq = faq.add_argument_group('Available Guides')


        #   How can i group it and make one of them a optional rather than required?
        faq.add_argument('-games', help ='-games --[game name] [--list for list of available guides]', nargs= "?" )
        faq.add_argument('-c', dest = 'credits', help = '%(prog)s Credential Center', action='store_true')
        faq.add_argument('-i', dest = 'info', help = '%(prog)s info Center', action='store_true')
        cmd = parser.parse_args(sys.argv[1:])

        
        try :

            if not cmd:
                raise Exception("404 : Command not found")

        except (ArgumentError, Exception) as e: 
            sys.exit(e)

        return cmd
    
    def Porgaminfo(self):
        return sys.exit(f"\n\nProgram name : {self.name}\nVersion : beta{self.version}\nDescription : {self.description}\n")

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