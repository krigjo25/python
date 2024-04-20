'''
Chapter 5 - Making your programming interactive.
Questions 1-10
'''

'''
Question 1

Determine the output of the following program without running the code:
a = 10
b = 4
print(a, "-", b, "=", a-b)
10 - 4 = 6
'''
a = 10
b = 4
print("Question 1 :\n ", a, "-", b, "=", a-b)

'''
Question 2

Rewrite the print() statement in Question 1
to display the same output using the % operator.
'''

a = 10
b = 4
c = a-b
print("Question 2 :\n module operator: %s-%s = %s"%(a, b, c))

'''
Question 3

Rewrite the print() statement in Question 1
to display the same output using the format() method.

'''
a = 10
b = 4
print("Question 3 :\n  Value of A :{0} Value of B : {1}" .format(a, b))
# Grunnen for at man ikke skal bruke , etter teksten, er fordi at funksjonen ikke existerer,
# men den er der for det som en illusjon, 
'''
Question 4
Determine the output of the following program without running the code:
print(\''Date:\n Jan 11, 2019 Time:\n1.28pm Venue:\nConvention Center Number of Pax:
\n30\'')
'''
print("Question 4 : \n \''Date:\n Jan 11, 2019 Time:\n1.28pm Venue:\nConvention Center Number of Pax:\n30\''")
###
'''
\''' Prints triple quoteationmarks,
\n prints a new line
'''
###
'''
Question 5

print('This is a single quotation (') mark and this is a double quotation (") mark.
')
The code above will result in a syntax error.
Make the necessary adjustment to correct it so that we get the following output:
This is a single quotation (') mark and this is a double quotation (") mark.
'''
print("Question 5 : \n This is a single quotation (\') mark, and this is a double quotation (\") mark.")


'''
Question 6
The code below shows the last few lines of a program:
print('Day 1 (%s): %s' %(day[1], venue[1]))
print('Day 2 (%s): %s' %(day[2], venue[2]))
print('Day 3 (%s): %s' %(day[3], venue[3]))
print('Day 4 (%s): %s' %(day[4], venue[4]))
print('Day 5 (%s): %s' %(day[5], venue[5]))
print('Day 6 (%s): %s' %(day[6], venue[6]))
print('Day 7 (%s): %s' %(day[7], venue[7]))
The lines before them are missing.

Add the missing lines so that the program prints the following output:
Travel Itinerary Day 1 (Tuesday): Tokyo to Osaka
Day 2 (Wednesday): Osaka to Kyoto
Day 3 (Thursday): Kyoto
 Day 4 (Friday): Kyoto to Nara
 Day 5(Saturday): Nara to Osaka
 Day 6 (Sunday): Osaka to Tokyo
 Day 7(Monday): Tokyo Hint: You need to use dictionaries in your solution.
'''
# Dictionary {Dictionary data: key} 1 ( which string / integer to get): key ( Which key to sends from
# Dictionrary data
day = {
    1:"Tuesday",
    2:"Wedensday",
    3:"thursday",
    4:"friday",
    5:"Saturday",
    6:"Sunday",
    7:"Monday"}
venue = {
    1: "Tokyo to Osaka",
    2:"Osaka to Kyoto",
    3:"Kyoto",
    4:"Kyoto to Nara",
    5:"Nara to Osaka",
    6:"Osaka to Tokyo",
    7:"Tokyo"}
print("Question 6 : \n Departures and arrivals")
print("The first trip (%s): from %s"%(day[1], venue[1]))
print("The Second trip (%s): from %s" %(day[2], venue[2]))
print("The third trip (%s): sleepover in %s" %(day[3], venue[3]))
print("The fourth trip (%s): from %s" %(day[4], venue[4]))
print("The fifth trip (%s): from %s" %(day[5], venue[5]))
print("The sixth trip (%s): from %s" %(day[6], venue[6]))
print("The seventh trip (%s): back to %s" %(day[7], venue[7]))
print("End of Departures and arrivals")
'''
 Question 7
 Write a program that uses the input() function to prompt the user to enter an integer.
 Store the user's input into a variable called num1.
 Next, prompt the user to enter another integer and store the input into another variable
 called num2.
 
 Use the print() function to display the following message:
 You entered * and ^ where * and ^ represent the two numbers entered by the user.
 For instance, the program may behave as shown below (user input is in bold italics):
 Please enter an integer: 5 Please enter another integer: 12 You entered 5 and 12
'''
print("Question 7 : \n Please insert your values")
a = input("Insert your first value : ")
b = input("insert the second value : ")
c = int(a) * int(b)
d = int(a)^int(b)

print("Question 7 : \n You entered %s and %s."%(a,b))
print("Question 7.1 : \n You entered %s * %s which equals = " %(a, b), c)
print("Question 7.2 : \n You entered %s ^ %s which equals =" %(a, b), d)

'''
 Question 8
 Use the input() function twice to prompt users to enter two integers and store the
 inputs into two variables called in1 and in2.

Use the int() function to cast the inputs into integers and store the results back into
in1 and in2. 
 Calculate the average of the two numbers and assign the result to a variable called average.
 The average is found by adding the two numbers and dividing the result by 2.
 Use the print() function to display the message The average is * where * represents the value
 of average, correct to two decimal places.
 For instance, the program may behave as shown below (user input is in bold italics):
 Please enter an integer: 3
 Please enter another integer: 10 T
 he average is 6.50
 '''

int1 = input("Enter one integer :")
int2 = input("Enter a new integer :")
x = int(int1)
num = int(int2)
result = x+num/2
print ("Numbers you entered : ", int1, "and ", int2, " the average of integers = ", result)
'''
Question 9
Write a program that prompts the user to enter his/her name.
The program then prompts the user to enter his/her favorite number using the prompt below:
Hi *, what is your favorite number?:
where * is to be replaced by the user's name.
Finally, the program displays the message *'s
favorite number is ^. where * represents the user's name and ^ represents his/her
favorite number. For instance, the program may behave as shown below
(user input is in bold italics): What is your name?: Jamie Hi Jamie, what is your
favorite number?: 111 Jamie's favorite number is 111.
'''
print(" Greetings what's your name? Any fav color?")
firstName = input("Type your firstname  : ")
favColor = input("Type your favorite colour. : ")
favInteger = input("Type your fav number : ")

print ("Greetings, ", firstName, "I really like that you like", favColor, " & the number ", favInteger)

'''
Question 10 Write a program that
uses a dictionary to store the following information about a city and the country that
it's in.
City, Country :

Chicago, USA
Los Angeles, USA
New York, USA
Osaka, Japan
Tokyo, Japan
Shanghai, China
Moscow, Russia
Paris, France
London, England
Seoul, South Korea

The program then prompts the user to enter a city name from one of the 10 cities above.
Based on the user's input, the program displays a message telling the user which country
the city is located in.
For instance, the program may behave as shown below (user input is in bold italics):

 Cities:
 Chicago,
 Los Angeles,
 New York,
 Osaka,
 Tokyo,
 Shanghai,
 Moscow,
 Paris,
 London,
 Seoul

 Please enter a city name from the list above: Osaka
 Osaka is located in Japan.
'''
# Defining the variable to cities
cities = " Choose between the following cities, \n Bergen, LosAngels, Tokyo,\n Shanghai, Osaka, Moscow, \n Paris, London, Seoul,\n Chicago, Ålesund & NewYork"
# Defining the dictionary for Countries
alC = dict(  Bergen = " is located in Norway",
             LosAngeles = "is located in United States of America",
             Tokyo = " is located in Japan",
             Shanghai = "is located in China",
             Osaka = "is located in Japan",
             Moscow = "is located in Russia",
             Paris = "is located in France",
             London = "is located in England",
             Seoul = "is located in South-Korea",
             Chicago = "is located in United States of America",
             Ålesund = "is located in Norway",
             NewYork = "is located in United States of America")

# Print the dictionary ; Cities, asks the user to choose between the cities.
print(cities, "\n")

#  prompts the user to choose a City which is provided
index = input("Choose one of the following cities : ")

# printing the choosen city
print(alC[index])

'''
 Question 11

 Write a program that prompts the user to enter 5 numbers,
 separating the numbers with commas. Calculate the sum of the 5 numbers and display the
 numbers entered and the sum to the user. For instance, the program may behave as shown
 below (user input is in bold italics): Please enter 5 numbers, separated by commas:
 23, 1, 12, 4, 5 You entered 23, 1, 12, 4, 5. The sum is 45.
 
 Hint: You can use the built-in Python method split() to work with the string input.
 For instance, the statement '1+24+51'.split('+') uses a plus sign (+) as the delimiter
 to split the string '1+24+51' into the list ['1', '24', '51']. For our question, you
 need to use a comma as the delimiter.
'''
###
index = input(" Enter five numbers, and seperate them by a comma : ")
result = index.split(",")
print ("You entered following numbers : %s, %s, %s, %s, %s, correct..?" %(result[0], result[1], result[2], result[3], result[4]))
print (" The sum of the values, is %d" %(int(result[0]) + int(result[1]) + int(result[2]) + int(result[3]) + int(result[4])))
