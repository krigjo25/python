'''
Chapter 8 : Working with Files

Question 1 :

Create a text file called ch8q1.txt with the following text :


Top Students:
Carol,
Zoe,
Andy,
Caleb,
Xavier,
Aaron,
Ben,
Adam,
Betty.

Write a simple program to read and display the first four lines from ch8ql.txt the output
Should not have any blank lines between each line.

For this question, you can assume that ch8q1 is in the same folder as the .py file

'''
 # openfunction(File name.codec, 'r'ead)
f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo textfiles\\ch8q1.txt', 'r')
fline = f.readline()
sline = f.readline()
tline = f.readline()
foline = f.readline()
print("Question 8.1 : \n \n", fline, sline, tline, foline)
f.close()
 # Boken sin del

f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo textfiles\\ch8q1.txt', 'r')
print("Book's version :\n")
for i in range(4):
    line = f.readline()
    print(line, end= "")
'''
Chapter 8 : Working with Files

Question 2 :

Suppose we have a text file called ch8q2.txt that contains an unknown
number of lines. Each line contains an Integer.

Write a program to read the integers from ch8q2 and sum all the positive
numbers. Display the result of the sum.

next, create the ch8q2.txt as follows:

12,
32,
15,
9,
16,
-3,
45,
-10

Run your code to verify it work as intended. For this question, you can
assume that ch8q2.txt is in the same folder as your py file.
For this question, you can assume that ch8q1 is in the same folder as the .py file

'''
 # openfunction(File name.codec, 'r'ead)
f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo textfiles\\ch8q2.txt', 'r')
sum = 0

print("\n Book's version : \n")

for line in f:
    if int(line) > 0:
        sum = sum + int(line)
        print(sum)


'''
Question 3 :

What is the difference between the "w" and "a" mode when using the
open() function to work with files?
'''
f = open('C:\\Users\\krigj\\Jottacloud\Kristoffer\\Documents\Projects\\Programming\Python\workbook\\demo textfiles\\ch8q3.txt', 'w')

f.write(" Diffrence between (W)riting and (A)ppend mode is \n")
f.write("W - mode : \n Truncate file to zero length or create a text file")
f.write("writing. The stream is positioned at the beginning of the file.")
f.write("file if the same name does not exist \n\n")
f.close()

f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\Python\\workbook\\demo textfiles\\ch8q3.txt', 'a')
f.write("A - mode. : \n Open for writing. The file is created if it Does")
f.write("Not exist. The stream is positioned at the end of the file. ")
f.write(" Subsequent write to the file will always end up at the then current ")
f.write("end of the file, irrespective of any intervening fseek(3) or similar")
f.close()

f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\Python\\workbook\\demo textfiles\\ch8q3.txt', 'r')
for i in range(8):
    line = f.readline()
    print(line, end= "")
f.close()

'''
Question 4 :

Write a function called getNumbers() that repeatedly promts the user
to enter an integer or enter "Q" to quite.

* Write the integers that the user entered into a text file called ch8q4.txt,
overwriting any previous data. You need to enuser that the user did
indeed enter an integer before writing the value into ch8q4.txt

* Next, write another function called findSum() that reads from ch8q4.txt,
adds up all the integers and returs the result.

Finally, call getNumbers() and findSum() and print the result returned
by findSum().

For this question you can assume ch8q4.txt is in the same folder as your
.py file. For instance the program may behave as shown below.

Enter an Integer or type "Q" to exit: 1.11
(Input is not an integer and will be ignored.)
Enter an integer or type "Q" to exit : 1
Enter an integer or type "Q" to exit : 12
Enter an integer or type "Q" to exit : 123
Enter an integer or type "Q" to exit : -1
Enter an integer or type "Q" to exit : asfa
(input is not an integer and will be ignored)
Enter an integer or type "Q" to exit : 11
Enter an integer or type "Q" to exit : Q
 # // Find the sum of get nummer ammount
def findSum(num):
    f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\demo textfiles\\ch8q4.txt', 'r')
    for line in f:
        if int(line) > 0:
            sum = sum + int(line)
            print(sum)
            return f.close()

def getNumber():
    num = 0
    while num != "Q":
            
        num = input('Type an integer or type "Q" to quit:  ')
        
        f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\demo textfiles\\ch8q4.txt','w+')
        f.write(num)
        if num == 'Q' or num == 'q':
            f = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\demo textfiles\\ch8q4.txt', 'r')

            for i in num:
                line = f.readline()
                print(line, end = "")
                findSum(num)
                f.close()
                break
getNumber()
findSum()
'''
'''
Question 5 :

Create a text file called stars.txt with a single line of 100 asterisks.

Use a for loop to read from the file and print the following output:

*

**

***

****

*****

******

*******

********

*********

**********

For this question, you can assume that stars.txt iis in the same folder as
your .py file.

'''
###

'''
Question 6 :

Suppose you have a folder on your C:\ drive called images. Inside the
Images folder you have a file called happy.jpg.

Write a program to read from C:\images\happy.jpg and write its content
to a new file called newhappy.jpg.

For this question you can write newhappy.jg to the same folder as your
.py file.

However, your .py file and happy.jpg should not be in the same folder
(i.e your .py file should not be in C:\Images folder).

Next, write a code to change the name of the new file from
newhappy.jpg and delete the original happy.jpg file from C:\images.
'''
import os

# Reading binary files such as non- texted 
inputFile = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\img\\demo.jpg', 'rb')
outPut = open('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\another demo img\\demo.jpg', 'wb')

 # Reading the file
readP = inputFile.read(10)

while len(readP):
    outPut.write(readP) # Reading the file
    readP = inputFile.read(10)
    
inputFile.close()
outPut.close()
pathD = os.path.join('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\img\\', 'demo.jpg')
pathR = os.path.join('C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\another demo img\\img\\demo.jpg', 'C:\\Users\\krigj\\Jottacloud\\Kristoffer\\Documents\\Projects\\Programming\\Python\\workbook\\demo\\another demo img\\img\\new-demo.jpg')
        
os.rename(pathR)
os.remove(pathR)
