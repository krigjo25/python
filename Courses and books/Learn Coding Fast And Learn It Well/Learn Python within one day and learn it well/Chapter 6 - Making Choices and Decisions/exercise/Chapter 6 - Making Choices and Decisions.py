'''
Chapter 6 Making Choices and Decisions
'''

'''
Question 1
State Which of the following Statements are true :

 (a) 2 > 5
 (b) 9 < 11
 (c) 7 >= 3
 (d) 8 <= 8
 (e) 10 != 12
 (f) 6 == 3
 (g) 4 > 2 and 7!=9
 (h) 3 > 1 and 9==9 and 1 > 2
 (i) 2 > 3 or 5 > 1
 (j) 3 > 1 or 5 == 5
 (k) 3 > 1 or 10 != 8 or 9 < 2


'''
print(" Qestion 1.1 \n A) Is 2 > 5 a true statement?")

a, b = 2,5
if a > b:
    print(" A is greater than b. This statement return true")
elif a < b:
        print(" A is less than b, so This statement returns false")
else:
    print("None correct")
    
print(" Qestion 1.2 \n B) Is 9 < 11 a true statement?")

a, b = 9,11
if a > b:
    print(" A is greater than b. This statement return true")
elif a < b:
        print(" A is less than b, so This statement returns false")
else:
    print("None correct")
    
print(" Qestion 1.3 \n C) Is 7 >= 3 a true statement?")

a, b = 7,3
if a >= b:
    print(" A is greater than or equal to B. This statement return true")
elif a <= b:
        print(" A is less than or equal to B, so This statement returns false")
else:
    print("None correct")
    
print(" Qestion 1.4 \n D) Is 8 >= 8 a true statement?")
a, b = 8,8
if a >= b:
    print(" A is greater than or equal to B. This statement return true")
elif a <= b:
        print(" A is less than B, so This statement returns false")
else:
    print("None correct")
    
print(" Qestion 1.5 \n E) Is 10 != 12 a true statement?")

a, b = 10,12
if a != b:
    print(" A is greater than b. This statement return true")
else:
    print("False")

a, b = 2,5
if a > b:
    print(" A is greater than b. This statement return true")
elif a < b:
        print(" A is less than b, so This statement returns false")
else:
    print("None correct")
 
print(" Qestion 1.6 \n G) Is 4 > 2 and 1 > 2 a true statement?")##
a, b = 4,2
c, d = 7,9
if a == b and c != d:
    print(" A equal to B. This statement return true")
else:
    print("False !")

print(" Qestion 1.7 \n H) Is 3 > 1 and 9 == 9 and 1 > 2 a true statement?")
a, b = 6,3
c, d = 9,9
f, g = 1,2
if a > b and c == d and f > g:
    print(" A is greater than B , C equals D and F is greater than G. This statement return true")
else:
    print("False !")

print(" Qestion 1.8 \n i) Is 2 > 3 or 5 > 1 a true statement?")
a, b = 2,3
c, d = 5,1
if a > b or 5>1:
    print("  true")
else:
    print("False !")
    
print(" Qestion 1.9 \n j) Is 3 > 1 OR 5 > 1 a true statement?")
a, b = 3,1
c, d = 5,1
if a > b or c > d:
    print(" A equal to B. This statement return true")
else:
    print("False !")

print(" Qestion 1.10 \n K) Is 3 > 1 or 10 !=8 a true statement?")
a, b = 3,1
c, d = 10,8
if a > b or c != d:
    print(" A equal to B. This statement return true")
else:
    print("False !")

'''
Question 2

Determine the output of the following program without running the code:

num = 5
if num == 1:
print('num is 1')
elif num == 2:
print('num is 2') else:
print('num is neither 1 nor 2')
'''
num = 5
if num == 1: # Returns false, since the variable aint either 1 or 2
 print('num is 1')
elif num == 2:
 print('num is 2')
else:
 print(' This returns false')
###
 '''
Question 3

Use the input() function to prompt users to enter an integer and use the int()
function to cast the input into an integer. Store the integer into a variable called
userInput.
 Next, write an if statement to perform the following tasks:

entered. If userInput is negative, multiply the number by -1 and assign it back to
userInput. Next, use the print() function to display the new value of userInput.
Finally, if userInput is zero, use the print() function to display the message
“You entered zero”. For instance, the program may behave as shown below
(user input is in bold italics):

Example 1:
Please enter an integer: 5 5

Example 2:
Please enter an integer: -2 2

Example 3:
Please enter an integer: 0
You entered zero
'''

userInput = int(input("Question 3 : \n Type an integer : "))
i = 0 
if userInput < i :
    userInput = str(userInput * -1)
    print(" Your result : -", userInput)
elif userInput > i:
    userInput = userInput* 1
    print ("Your result : ", userInput)
elif userInput == 0:
    print(" You entered zero")
else:
    print(" An error occured during looping")
    
'''
Question 4

Use the input() function to prompt users to enter an integer from 0 to 100 inclusive,
cast the input into an integer and store the integer into a variable called testScore.
 Use an if statement to display the grade that corresponds to testScore based on the
 following table:
 70 to 100: A
 60 to 69: B
 50 to 59: C
 0 to 49: Fail
 Smaller than 0 or greater than 100: Invalid

 For instance, the program may behave as shown below
 (user input is in bold italics):
Example 1: Please enter an integer from 0 to 100 inclusive: 20 Fail
Example 2: Please enter an integer from 0 to 100 inclusive: 54 C
Example 3: Please enter an integer from 0 to 100 inclusive: -5 Invalid
'''
   
testScore = int(input(" Question 4: \n Choose a number between : \n 0 and 100 : "))
if testScore <= 50:
    print( "Test not approved grade F, test score", testScore)
elif testScore <= 60:
    print("Test Apporved with grade C, test score : ", testScore)
elif testScore <= 70:
    print("Test Approved with grade B, test score : ", testScore)
elif testScore <= 100:
    print("Congratulation you got the grade A, with", testScore, "of 100")
elif testScore < 0 or testScore > 100:
    print("Your Score is invalid")

'''
Question 5

Determine the output of the following program without running the code:
 num = 5
 print('Orange Juice' if num == 5 else 'Peanut Butter')
'''
num = 5
if num == 5:
 print('Orange Juice')
else:
    print('Peanut Butter')

'''
Question 6

Use the input() function to prompt users to enter an integer, cast the input into an
integer and store the integer into a variable called num1.
 Write an inline if statement to print the message “Odd” or “Even”
 depending on whether num1 is odd or even.
 
 Hint: num1 is even if the remainder is zero when it is divided by 2.
 For instance, the program may behave as shown below (user input is in bold italics):
 Example 1:
 Please enter an integer: 9
 Odd

 Example 2:
 Please enter an integer: 18
 Even
'''
userInput = int(input("Type an Integer and we'll check if it's odd or even :"))
num = userInput % 2
if num == 1:
    print("The number is even")
else:
    print("The number is odd")
'''
Question 7

Given that myNumbers = [1, 21, 12, 45, 2, 7], use a for loop to print the elements in the
list one by one.
'''
myNumbers = [1, 21, 12, 45, 2, 7]
for i in myNumbers:
    
    print(i)

'''
Question 8
 Given that marks = [12, 4, 3, 17, 20, 19, 16], use a for loop to find the sum of the
 numbers in the list.
 Use the print() function to print the sum.
   print(i)
'''
marks = [12, 4, 3, 17, 20, 19, 16]
for i in marks:
    i = sum(marks)
print("the sum of the variable is : %d " %(i))

'''
Question 9
 Given that classRanking = ['Jane', 'Peter', 'Michael', 'Tom'], use a for loop and the
 enumerate() method to display the following output:
 1      Jane
 2      Peter
 3      Michael
 4      Tom
 Each line consists of a number, followed by a tab and a name.
 '''
classRanking = ['Jane', 'Peter', 'Michael', 'Tom']
for index, cRanking in enumerate(classRanking, 1): #Adding numbers to strings
    print(index, cRanking)

'''
Question 10
Question 10 Given that testScores = {'Aaron':12, 'Betty':17, 'Carol':14},
write a for loop that gives us the following output:
 Aaron scored 12 marks.
 Betty scored 17 marks.
 Carol scored 14 marks.
'''
testScores = {'Aaron':12, 'Betty':17, 'Carol':14}
for i in testScores:
    print("Scoreboard : \n %s Scored %d marks. \n" % (i, testScores[i]))

'''
Question 11
Determine the output of the following code without running the code:
ages = {'Abigail':7, 'Bond':13, 'Calvin':4}
for i, j in ages.items():
 print('%s\t%s' %(j, i))
''' 
ages = {'Abigail':7, 'Bond':13, 'Calvin':4}
for i, j in ages.items():
 print('%s\t%s' %(j, i)) ## Same as Question 10 just an Alternative way key:dictonary key

'''
Question 12
Determine the output of the following code without running the code:
message = 'Happy Birthday'
for i in message:
if (i == 'a'):
 print('@')
else: print(i)
'''

message = 'Happy Birthday'
for i in message: # 'i' becomes '@'
    if (i == 'a'):
         print("@")
    else:
        print(i)
## Printing the message with one word each line

'''
Question 13

Determine the output of the following code without running the code:
 (i) for i in range(10):
 print (i)
 (ii) for i in range(2, 5):
 print(i)
 (iii) for i in range(4, 10, 2):
 print(i)

'''
# Explaination
'''
For ( Starter en loop fordi ) i (variabelen) in (i) range(10) ( rekken til 10 )
For starter en loop fordi variabelen i, i rekken teller fra 0 - 10
dereter printer kommandoen print variabelen som har funksjonen.
'''
for i in range(10): # Counting from 0 - 9
 print (i)
 if i == 0:
     print('Question 13')

for i in range(2, 5): # the for loop counting from 2-4
 print(i)

for i in range(4, 10, 2): # Starting at four  to ten, but each second
 print(i)

'''
Question 14

Explain what is wrong with the following code:
 i = 0
 while i < 5:
 print('The value of i = ', i)
 
 Modify the code so that it produces the following output:
 The value of i =  0
 The value of i =  1
 The value of i =  2
 The value of i =  3
 The value of i =  4
 '''
### The Variable is alaways zero so it will never be greater than 5 ###
i = 0
'''
HOW WHILE LOOPS WORK
While i is less, greater or equal to 5
Do the task, if variable never gets updated infinite loop occours.
So always update the shitty variable.
'''
i= 0
while i <= 5:
    print(" Question 14.1 : \n The value of i = ", i)
    i = i + 1

'''
Question 15

Determine the output of the following code without running the code:

i = 5 while i>0:
 if i%3 == 0:
  print(i, 'is a multiple of 3')
  else: print(i, 'is not a multiple of 3') i = i - 1


 '''
# The output of the code. First two 
i = 5
while i>0: ### While i is greater than 0 Do the task
    if i % 3 == 0: ### If i % 3 == 0 print the output 
        print(i, 'is a multiple of 3')
        break ### Program ends
    else: # Else print the next statement
        print(i, 'is not a multiple of 3') 
        i = i - 1 # Reduce the variable with one each time, the if statement doesnt work
# But the output will be infinitive

'''
Question 16

Write a while loop that repeatedly prompts users to enter a number or enter “END” to exit.
 After the user enters the number, the while loop simply displays the number entered.
 If the user enters “END”, the program displays the message “Goodbye!” and ends.
 For instance, the program may behave as shown below (user input is in bold italics):

 Enter a number or END to exit: 3
 3

 Enter a number or END to exit: 123
 123

 Enter a number or END to exit: -2
 -2

 Enter a number or END to exit: END

 Goodbye!
'''

'''
My version :
'''
while 1 > 0: # While 1 is greater than 0 do the task below
    userInput = input('Type a number or type "END" to exit the program : ')
    end,stop,pexit = "END", "end", "exit" # KILLS the program
    if userInput == end or userInput == stop or userInput == pexit: # Check if imposter is killing
        print("Good bye sir !")
        break # STOP
    else: # or send this
        print("Numbers entered : ", userInput)

'''
Easier way with only While
'''
uInput = input('Type a number or type "END" to exit the program :')
while uInput != 'END':
    print("Your input : ", uInput)
    uInput = input('Type a number or type "END" to exit : ')

print('Good bye !')


'''

 Question 17
 Write a while loop that repeatedly prompts users to enter a positive
 integer or enter -1 to exit. 
 After the user enters the integer, the while loop should display the sum of all numbers
 entered so far. If the user enters -1, the program displays the message “Goodbye!”
 and ends.
For instance, the program may behave as shown below (user input is in bold italics):

Enter a positive integer or -1 to exit: 3
 Sum = 3
 
 Enter a positive integer or -1 to exit: 5
 Sum = 8
 
 Enter a positive integer or -1 to exit: 1
 Sum = 9
 
 Enter a positive integer or -1 to exit: -1
 Goodbye!

 '''
sum = 0
i =int(input('Type a number or type -1 to exit the program : ')) # Input  
while i != -1: # While condition is true do the task
     sum += i
     print("sum = ", sum)
     i = int(input('Type a number or type -1 to exit the program : '))
print (' Good bye sir')


'''
 Question 18
 
Modify the code in Question 17 so that if the user enters a non positive integer
(other than -1), the program displays the message “You entered a non positive integer”
and does not add the number to the sum. For instance, the program may behave as shown
below (user input is in bold italics):

 Enter a positive integer or -1 to exit: 3
 Sum = 3

 Enter a positive integer or -1 to exit: 5
 Sum = 8

 Enter a positive integer or -1 to exit: -2
 You entered a non positive integer Enter a positive integer or -1 to exit: 4
 Sum = 12
'''

sum = 0
i =int(input('Type a number or type a negative number to-1 to exit the program : ')) # Input  
while i != -1: # While condition is true do the task
    if i > 0:
     sum += i
     print("sum = ", sum)
     i = int(input('Type a number or type -1 to exit the program : '))
    else:
         print (" The number you entered is not an positive integer !")
         i = int(input('Type a number or type -1 to exit the program : '))
print (' Good bye sir')
#--------------------------------------------------------------------------------

sum = 0
i =int(input('Type a number or type a negative number to-1 to exit the program : ')) # Input  
while i != -1 : # While condition is true do the task
    sum += i
    print("sum = ", sum)
    i = int(input('Type a number or type -1 to exit the program : '))
    while i < -1:
         print (" The number you entered is not an positive integer !")
         i = int(input('Type a number or type -1 to exit the program : '))
print (' Good bye sir')



'''
 Question 19

Write a program that prompts the user to enter two integers.
Suppose the integers are p and q. The program then prints p rows of q asterisks.
For instance, the program may behave as shown below (user input is in bold italics):

Please enter the number of rows: 5
Please enter the number of asterisks per row: 10
 **********
 **********
 **********
 **********
 **********
Note:
By default, the print() function adds a new line at the end of its output.
If you do not want that to happen, you have to pass in end = '' to the print() function.
This will remove the new line. Note that '' is made up of two single quotes, not a single
double quote.

For instance,

print('A')
print('B')

gives us A B while print('A', end = '')

print('B', end = '') gives us AB

'''
# Inputs | My version

numrow = int(input('Enter the numbers of rows : '))
numas = int(input('Enter the number of asterisks per row : '))

 # If the rogram detects there is less or zero rows run
while numrow != 0:
    # Variable declearation
      # Asterisks
    ast = '*'
    asterisks = ast * numas
 # While there is still numbers in row substract one row
    numrow = numrow - 1
    print(asterisks)
#----------------------------------------------------------------------
# Books version :
                 # INPUTS
numrow = int(input('Enter the numbers of rows : '))
numas = int(input('Enter the number of asterisks per row : '))

        # For loops
for i in range(numrow): # For i ( New variable)  
    for j in range(numas): 
        print( '*', end =")
    print()


'''
Question 20
Write a program that prompts the user to enter a short message.
The program then replaces the first three occurrences of the letter “a” in the message
with “@” and subsequent occurrences of the letter “a” with “A”. Finally, the program
displays the new message. For instance, the program may behave as shown below

(user input is in bold italics): Please enter a message:

Python is an excellent language to learn for both beginners and experienced programmers

result:

Python is @n excellent l@ngu@ge to leArn for both beginners And experienced progrAmmers
'''
## Books version
o = 0
uInput = input(' Write us a feedback : ')
for i in uInput: # For loop
    if i == "a": # if i equals a
        o = 0 + 1 # then o = 0 add one more
        if 0 <=3:  # When o <= 3 Print below
            print('@', end = "")
        
        else: 
         print('A', end="")
         # End of inner if statement
    else:
        print(i,end="")
    # End of outter if statement
print(uInput)

'''
Question 21

Write a program that uses a for loop to prompt the user to enter 10 numbers.
The program then finds the smallest and largest number and displays the result to the user.
For instance, the program may behave as shown below (user input is in bold italics):

First
While, for or IF
If blir for mye hardkoding
for 
Please enter number 1 : 5
Please enter number 2 : 12
Please enter number 3 : 2
Please enter number 4 : 3
Please enter number 5 : -1
Please enter number 6 : 5.7
Please enter number 7 : 11
Please enter number 8 : 111
Please enter number 9 : 0

Please enter number 10: -3.9
The smallest numver is : -3.9
the largest number is : 111
'''
print("This program you're suppost to enter five different number, not at once, but in each input")
'''
For å gjøre koden mest mulig effektiv, må vi bruke for loop for å gå igjennom listen med
inputs 
'''
for i in range(10):
    uInput = input( 'Number %s : ' % (i + 1))
    if i == 0:
        lnr, snr = uInput, uInput
    elif float(uInput) > float(lnr):
        lnr = uInput
    elif float(uInput) < float(snr):
        snr = uInput
print ("Smallest number is : %s" % (snr))
print ("The largest number is %s" %(lnr))
##### Forklar hvorfor !
