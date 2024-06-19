#   Importing responsories
#   Importing responsories
import validators as v

def main():
  print(Validation(input('What is your e-mail addres?')))

def Validation(arg):

  '''
      #   Author : krigjo25
      #   Date : 07.11-22

      #   Use either validator-collection or validators library.
      #   Implement a program that prompts the user for an email addres then prints Valid or Invalid.
      #   If the input is a syntatically valid email address. You may not use re.
      #   Do not validate whether the email address’s domain name actually exists.

  '''
  # Initializing list
  if not v.email(arg): return 'Invalid'
  elif v.email(arg): return 'Valid'
  else:
    return 'something went wrong'


if __name__== '__main__':
  main()
