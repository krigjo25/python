#   Importing responsories
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, ArgumentError


class CommandlineInterface():

    '''
        The command line Interface
    '''
    version = "0.0.1"
    author = "krigjo25"
    name = "IntegerGames"
    description = "Collection of Integer Games"

    def CommandLineOptions(self):

        '''Constructing the argparser'''
        #   Creating a argumentParser
        parser  = ArgumentParser(prog = self.name, formatter_class= ArgumentDefaultsHelpFormatter, description= self.description, epilog= f"{self.version} - by {self.author}")

        
        #   Initializing The helper interface
        parser.add_argument('-i', '--info', dest = 'info', help = '%(prog)s info Center', action='store_true')
        parser.add_argument('-gtn', '--guessthenumber', dest = 'gtn', help ='urls to check', action='store_true')
        parser.add_argument('-c', '--credits', dest = 'credits', help = '%(prog)s Credential Center', action='store_true')
        parser.add_argument('-tlp', '--proffessor', dest = 'tlp', help ='The mathematical game The Little Proffessor', action='store_true')
        

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
        
        """
            Libraries used in the project :\n
            sys - Python built-in responsories\n
            random - Python built-in responsories\n
            argparse - Python command line tool responsories\n
        """
        return sys.exit("""
            Libraries used in the project :
            pytest - pytest - by pytest team
            sys - Python built-in responsories
            random - Python built-in responsories
            argparse - Python command line tool responsories\n
            
            Project Created by : @krigjo25
            Copyrights all rights reserver 2024
        """)