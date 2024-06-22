
def  MathInterPreter():

    #   Prompting the user for an artihmetic expression
    prompt = input('Write a mathematic challange :')

    # Handling the prompt
    x, y, z = prompt.split(' ')

    #   Converting the string into integers
    x = int(x)
    z = int(z)

#   Checking wheter the y matches any of the cases.
    match y:

        case '+':
            x += z

        case '-':
            x -= z

        case '/':
            x /= z

        case '**':
            x **= z

        case '*':
            x *= z

    #   Returning the result
    return print(float(x))

MathInterPreter()
