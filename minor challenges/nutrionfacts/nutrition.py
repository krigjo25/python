def main():

    """
        Title       :   Nutrition Facts
        author      :   krigjo25
        Description :
            A program that returns calories of a inputted fruit.

            USEAGE :    In the terminal type nutrition.py
            Follow the instruction for the prompted message.
    """
    #   Initializing a dictionary
    fruits = {
                    'kiwifruit':90,
                    'lemon': 15,
                    'apple':130,
                    'grapes':90,
                    'orange':80,
                    'peach': 60,
                    'pear': 100,
                    'avocado':50,
                    'banana':110,
                    'honeydew':50,
                    'pinapple':50,
                    'tangerine':50,
                    'nectarine':60,
                    'cantaloupe':50,
                    'grapefruit':60,
                    'watermelon':80,
                    'strawberries':50,
                    'sweet cherries':100
    }

    while True:

        #   Initializing an input
        fruit = str(input('Fruit :')).lower()

        try :

            #   Ensure the fruit is letters and is in the dictionary
            if fruit.isdigit() or fruit not in fruits: raise ValueError()

        except ValueError as e:

            return e

        return print(f'Calories : {fruits.get(fruit)}')

if __name__ == '__main__':
    main()
