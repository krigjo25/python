#   Prompting the user with a input
prmpt = input('prompt : ')

# Handling the user prompt

for i in prmpt:

    #   Converting camelcase to snakecase
    if i != i.lower():
        i = f'_{i}'.lower()

    print (i, end='')
