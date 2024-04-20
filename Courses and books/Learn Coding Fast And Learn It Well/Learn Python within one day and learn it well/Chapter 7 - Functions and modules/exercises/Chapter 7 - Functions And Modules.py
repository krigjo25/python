'''
Chapter 7 - Functions and modules


Question 1

Question 1 Write a function called greetUser() that simply displays the message
“Hello World” to users. After coding the function,

write a statement to call the function.
'''
def greetUser(): # Defines a function 
    print("Question 1 :\n Geetings, Python") # Prints out the message
    return # return
greetUser() # Calls the function

'''
Question 2

Write a function called greetUserByName() that prompts the user for his/her name
and displays the message Hello ^ where ^ represents the name entered by the user.

After coding the function, write a statement to call the function.
'''
def userName():
    #Variables
    uName = input("Type your name: ")
    
    # Print
    print("Question 2 :\n Greetings", uName, ", Thank you very much for your registeration")
    return

userName()
'''
Question 3

Write a function called displayMessage() that has one
parameter greetings. Within the function, use the print()
function to display the value of greetings.

After coding the function, write a statement to call the function using 'Good Morning'
as the argument.
'''
def displayGreeting(greeting): # Defined function with a parameter
    print("Question 3 : \n,", greeting) # Printing the parameter
    return
# Calling the function with a parameter

displayGreeting("Hello Python Universe")

'''
Question 4

Write a function called calculateQuotient() that has two parameters a and b.
Within the function, write a return statement to return the value of a/b.

After coding the function,
write a statement to call the function using 12 and 3 as the arguments.
Asign the result to a variable called result and print the value of result
'''
 
def calQuotient(a,b):
    result = a + b
    print("Question 4:\n Value of the parameters  a(",a,") + b(",b,") = ", result)
    return result

calQuotient(14,12)

'''
Question 5

Modify the function in the previous question to include error handling using a try-except
statement. Return -1 when an error occours. Call this new function calculateQuotient2()

After coding the function, write a statement to call the function using

(i) 12 and 13 as the arguments,
(ii) 5 and 0 as the aruments,
(iii) 'abcd' and 2 as the arguments.

For each of the cases above, assign the result to a variable called result and print the
value of result
'''

# Question 5.1 
def calcQuotient(a,b):
    try:
        result = a + b
        print("Question 5.1 :\n Value of the parameters = ", result)
    except:
        print("Attention ! an error occured during the procsess")
        return -1
calcQuotient(12,13)

# Question 5.2
def calcQuotient(a,b):
    try:
        result = a + b
        print("Question 5.2 :\n Value of the parameters = ", result)
    except:
        print("Attention ! an error occured during the procsess")
        return -1
calcQuotient(5,0)

#Question 5.3
def calcQuotient(a,b):
    try:
        result = a + b
        print("Question 5.3 :\n Value of the parameters = ", result)
    except: # Sends out an error message
        print("Attention ! an error occured during the procsess, discovered a string")
        return -1
    
calcQuotient("abcd",2)


'''
Question 6
Write a function called absValue() that accepts a numerical input
(The input can include decimal values).

* If the input is zero or positive it simply returns the number. (x)
* If the input is negative, it multiplies the number by -1 and returns the
result.
* If the input is non numerical, it returns -1

After coding the function, call the function with the following inputs and print the results:
12
5.7
0
-4
-5.2
'abc'
'''
'''
Question 6
Write a function called absValue() that accepts a numerical input
(The input can include decimal values).

* If the input is zero or positive it simply returns the number. (x)

* If the input is negative, it multiplies the number by -1 and returns the
result.

* If the input is non numerical, it returns -1

After coding the function, call the function with the following inputs and print the results:
12
5.7
0
-4
-5.2
'abc'
'''


def absValue(a):
 try:
     num = float(a)
     
     if num >= 0:
      return a

     else:
      return -1*a
    
 except Exception as e:
     return -1

result = absValue(12)
print(" Question 6.1 \n", result, "\n")

result = absValue(5.7)
print(" Question 6.2 \n", result, "\n")

result = absValue(0)
print(" Question 6.3 \n", result, "\n")

result = absValue(-4)
print(" Question 6.1 \n", result, "\n")

result = absValue(-5.2)
print(" Question 6.1 \n", result, "\n")

result = absValue('abc')
print(" Question 6.1 \n", result, "\n")

'''
Question 7

Determine the output of the following code with out running the code:

a = 1
def displayNumbers():
 a = 2
 print (a)
'''
a = 1
def displayNumbers():
 a = 2
 # The output will be 2 since the variable is overwritten only with-in the code
 print("Question 7: \n the value of the variable is = ", a)

 '''
Question 8

Explain what is incorrect with the following code:

deffunctionwithb():
b = 1
print(Question 8: \n what were incorrect where the we didnt define it first")
print(b)
'''
def functionwithb():
    b = 1
    print("Question 8: \n what were incorrect where the we didnt define it first")
    print("Variable = ", b)
functionwithb()

'''
Question 9

Determine the output of the following code without running the code:

def calProduct(a,b,c = 1, d = 2)
    product = a*b*c*d
    print("Question 9: \n The value of the  product is = product")
calProduct(2,3)
calProduct(2, 3, 4)
calProduct(2, 3, 4, 5)
'''

def calProduct(a,b,c = 1, d = 2):
    product = a*b*c*d
    print("Question 9: \n The value of the  product is =", product)
    
#  2 *3 *1 * 2
calProduct(2,3)

# 2 * 3 * 4 * 2
calProduct(2, 3, 4)

# 2 * 3 * 4 * 5
calProduct(2, 3, 4, 5)

'''
Question 10

The statements below show the function teamMembers() being called with different arguments:

Function call:
TeamMembers('Jane', 'Jhon')

The output:
The team members are Jane, Jhon, James and Kelly.

Function Call:
TeamMembers('Peter', 'Jack')

The output:
The team members are Peter', Jack, James and Kelly

Function call:
teamMembers('Peter', 'Jhon', 'Ben')

The output
The team members are Peter, jhon, Ben and Kelly

Function Call:
TeamMembers('Jamie', 'Adam', 'Calvin', 'Danny')

The output:
The team members are Jamie, Adam, Calvin and Danny.

Code the teamMembers() function to get the outputs shown and run it to verify that your
function performs correctly
'''
# First
def teamMembers(a,b,c = 'James', d = 'Kelly'):
    '''
        # We've got 4 parameters which shall be filled.
        # First three is not decided what the parameters contain.
        # Third, fourth is filled with information.
    '''
    print("Our crew : \n %s %s, %s, %s"% (a, b, c, d))
        
teamMembers('Jane', 'Jhon',) # +2 two of the pre filled parameters

teamMembers('Peter', 'Jack')

teamMembers('Jane', 'Jhon', 'Calvin')  #third is replaced with Calvin

teamMembers('Kelly', 'Bito', 'Patrica', 'Danny') 

'''
Question 11

Determind the output of the following code without running the code:

def findSum(*a):
    sum = 0
    for i in a
        sum = sum + i
        print(sum)
findSum(1, 2, 3)
findSum(1, 2, 3, 4)
'''
def findSum(*a): # Defining a custom function, the asteristisk implys that this
                 # is a non-keyworded variable lengt argument list
    sum = 0
    for i in a: #For (loop) i in non-keyworded VLAL
        sum = sum + i # Adds the numbers together
        print(sum) # printing out the inputs
findSum(1, 2, 3)
findSum(1, 2, 3, 4)
'''
Question 12

The statements below show the function printFavColor() being called with different
arguments

Function Call:
printFavColor('Yellow', 'Green')

The output :

Your favorite colors are:
Yellow,
Green.

Function Call:
printFavColor('Orange', 'Pink', 'Blue')

The output:

Your favorite colors are:
Orange,
Pink,
Blue

Code the printFavColor() function to get the outputs shown and run to verify that your
function performs correctly.
'''

def favColor(a,b,c = ''):
    '''
    # Incase the first argument has only one parameter, we give them values so they can be replaced
    # If we add arguments to the parameter, we'll choose how many we'll need

    '''
    # Adding the parameters to the variable
    favColor = a,b,c

    # Creating a for loop so we can loop through the parameters with only one variable, and
    # List them.
    print ("Question 12 :\n \nFavorite colours" )
    for i in favColor:
     print(i)
    return a,b,c

# Favoritecolour 
favColor('Yellow,', 'Green' )

favColor('Orange,', 'Pink', 'Blue' )

'''
Question 13 :

The statement below show the function printNamesAndGrades() being called with different
arguments.


Function Call:

printNamesAndGrades (Adam = 'C', Tim = 'A')

Output :

Name | Grade

Adam : C

Tim : A


Function Call:

printNamesAndGrades (Adam = 'C', Tim = 'A')

Output :

Name | Grade

Sam : A-

Lee : B

Joan : A+

Code the printNamesAndGrades() function to get the outputs shown and run it to verify that
Your function performs correctly.
'''

# Definining the custom function called nameGrade
def nameGrade(**grade):
    '''
    # Dubble arterisks denote that this parameter has stored
    # A keyworded variable-length argument list
    # Which is equal to a dictonary.
    '''
    print('Question 13 :\n')
    for n,g in grade.items():
        print(" Student : %s, %s "% (n,g))
    print("\n")
    return 



#Callback tot the function to show the grade for the student(s)

nameGrade (Adam = 'C', Tim = 'A')

nameGrade (Sam = 'A-', Lee = 'B', Joan = 'C')

'''
Question 14 :

Explain what is wrong with the following code :

Custom funtion :

def varlength('*b,a,**c)
    '''
    # The issue were discovered in the custom function's parameters
    # A key-worded argument or a non-key worded argument has to be at the end of the function
'''
    print(a)
    
    for i in b:
        print(i)
        
    for j,k in c.items():
        print (j, "scored :", k)
    return 


Modify the varlength() function so that the statement:

varlength('Jane', 2,3,4, Apple = 'A', Betty = 'B')


Producing the following output:

Jermey
2
3
4
Apple Scored A
Betty Scored B

Run the program  to verify that your function performs correctly.
'''

# Custom function
def varlength(a,*b,**c):
    print(a)
    
    for i in b:
        print(i)
        
    for j,k in c.items():
        print (j, "scored :", k)
    return



# Calling the function
varlength('Jane', 2,3,4, Apple = 'A', Betty = 'B')

'''
Question 15 :



Write a function called sumNumbers()
that has two parameters, target and *b.

The function checks if there exist any two numbers in b that add up to target.
if two numbers are found, the function displays an equation showing the addition.

If no no numbers are found, the function prints the message :
"No results found"

For instance, the statements below show the function being called with different arguments:



Function Call:

sumNumbers(5, 3, 1, 4, 2)


Output :
 b 3 + 2 = 5

For this example, even though there can be more than one way to get the target 5
( 1+ 4 and 3 + 2), the function is only required to display one equation.

Try coding this function and run it to verify that it performs correctly.


Hint :

You can access the numbers in b using the list notation. For instance, for the function call

sumNumbers(5,3,1,4,2)

Target = 5

b[0] = 3
b[1] = 1
b[2] = 4
b[3] = 2

'''

    #Defining a custom function with two parameters, Target and a non-keyworded argument,
def sumNumbers(target, *b):
    sum = 0
    b = list(b)
    del(b[1])
    del(b[1])
    
        # For (loop) i in b 
    for i in b:
     sum = sum + i
     
        # If sum == target print
    if sum == target:
            print("b = ", target)
            
        #   Else 
    else:
            print("No numbers equal to target found, retry")
    return
        # It won't work due to 5 is the target and 3 + 1 + 4 + 2 = 10
sumNumbers(5, 3, 1, 4, 2)


'''
Question 16 :

The statements below show the function

countryCapital() being called with different arguments.



Function Call:

countryCapitals(Germany = 'Berlin')

Output :

The Capital of Germany is Berlin.

Function Call:

countryCapitals(USA = 'Washington D.C,' China = 'Beijing')

Output :

The Capital of USA is Washington D.C, China  is Beijing

Function Call:

countryCapitals(Japan = 'Tokyo', Indonesia = 'Jakarta', France = 'Paris')

Output :

The Capitals of Japan, Indonesia and France are Tokyo, Jakarta and Paris respectively.

Code the countryCapitals() function to get the outputs shown and run it to verify that your
function performs correctly.

Note:

Note that the output Produced by this function differ depending on the number of countries
passed in. For instance, if there's only one country, the singular form is used
(e.g capital is) that you accessing when you loop through a dictionary.


Hint :

You can use the len() method to fin the number of items passed in to the countryCapital()
function.

In addition, recall that you can use the enumerate() method to determine
the index of the item For instance, if the dictionary is

capitals =
{'USA':'Washington, D.C', 'United Kindom': 'London', 'China':'Beijing', 'Japan':'Tokyo',
'France':Paris'}

and we use for i in enumerate(capitals):
to loop thorugh the capitals dictionary, it gives us the index of the current item while j
gives us the dictionary key of the item in other words, when i = 0, j = 'USA'.



'''

'''
# Defining a custom function
def countryCapitals(**cities):
    
    # For loop to loop through countries and cities
        b = cities.items()  
        a = enumerate(cities)

        for nr, country, in a:
            
         for country, i in b:
            if nr == 0:
                print("The Captital of %s is located in %s \n"% (country, i))
        for d,e in b:
            if nr <= 1 or nr :
                print("The capitals of %s, %s,"%(d, e))
            else:
             return 

####
'''
# Boka
            #   Custom Function
def countryCapitals(q, **cities):
    if(len(cities)== 1):
        print("The capital of ", end= ' ' )
    else:
        print("The captials ", end= ' ')

    # Print the country name
    for i, j in enumerate(cities):
        if i == 0:
            print(j, end = '')
        elif i == len(cities)-1:
            print("and %s " % (j), end = ' ')
        else:
            print(", %s " % (j), end = ' ')

        # Print the Capitals
        for i, j in enumerate(cities):
            if i == 0:
                print(cities[j], end = ' ')
            elif i == len(cities)-1:
                print("and %s " % (cities[j]), end = ' ')
            else:
                print(", %s " % (cities[j]), end = ' ')

            if len(cities) == 1:
                print(".")
            else:
                print("respectively")

             
countryCapitals("Question 14.1 : ", Germany = 'Berlin')

# q 14.2
countryCapitals("Question 14.2 : ", USA = 'Washington D.C,', China = 'Beijing')

# q 14.3
countryCapitals("Question 14.3 : ", Japan = 'Tokyo', Indonesia = 'Jakarta', France = 'Paris')

import demo
import demo as d
from demo import func1, func2
import sys

'''
Question 17

Suppose you have a file called myfunction.p with the following code:

def func1():
    print("This is a simple function")

def func2(message):
    print(message)

The statements below show three ways of using functions from myfunctions.py inside another
Phyton file stored in the same folder.
Write down the correct import statement for each of them


Question 17.1

myfunctions.func1()

myfunctions.func2()

Question 17.2

f.func1()

f.func2(jello)

Question 17.3

func1()

func2('Hello')

Question 18

Now suppose we want to use func1() and func2() from the previous question inside a py file
that is NOT in the same folder as myfunctions.py and it is stored in Python-files, folder

What code must we add to this new python file so we can continue to use the two functions
'''

#   Variable | file.py | function
func1, func2 = demo.func1("Question 17.1 : \n"), demo.func2("Hello World !\n")
func1, func2 = d.func1("Question 17.2 : \n"), d.func2("Hello World !\n")
func1, func2 = d.func1("Question 17.3 : \n"), d.func2("Hello World !")

# Question 18

if'C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python' not in sys.path:
    # Searching the folder if not in the system path
    # search this folder
    sys.path.append('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo')

#if'C:\Users\krigj\Jottacloud\Kristoffer\Documents\Projects\Programming\Python\workbook\demo' not in sys.path
#sys.path.append('C:\Users\krigj\Jottacloud\Kristoffer\Documents\Projects\Programming\Python\workbook\demo')