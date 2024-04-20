#   Importing the module os
from os import rename, remove

#   Defining the function
def UpdateScore(user, name, score):

    #   Checking if user is true
    if bool(user) == True:

        with open('txt/Scores.txt', 'a') as f:

            #   Initializing a variable
            txt = f'{name}      {score}'

            #   Appending the text
            f.write(txt)

            #   Close the file
            f.close()

    else:

        with open('txt/Scores.tmp', 'w') as f:

            f.write()

    return
UpdateScore('Haje')