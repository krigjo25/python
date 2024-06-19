#   Importing responsories
'''
    Title : Figlet
    Description :   A program to

    Base by :
    Developed by : @krigjo25
    Date Started : 25.11-23
    Date Submited : 25.11-23
    Date re-Submited : N/A

'''
import sys
from pyfiglet import Figlet, FontNotFound

def PyFiglet():

    arg = ['-f', '--font']
    f = Figlet()

    try :

        if len(sys.argv) > 1 and sys.argv[1] in arg:
            f = Figlet(font=sys.argv[2])
            prmpt = input('prompt : ')
            print(f.renderText(prmpt))
            sys.exit()

    except (FontNotFound, ValueError) as e:

        #   Exception error
        sys.exit(f'Invalid usage')

    if len(sys.argv) == 1:
        prmpt = input('prompt:')
        print(f.renderText(prmpt))

if '__name__' == '__main__':
    PyFiglet()
