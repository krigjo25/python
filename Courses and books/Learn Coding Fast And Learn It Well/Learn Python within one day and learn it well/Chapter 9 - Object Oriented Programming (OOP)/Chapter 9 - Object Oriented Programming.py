'''
Chapter 9 - Object Oriented Programming Part 1

'''
            #Question 1
from oopp import VehicleImpound
            # Question 2
from oopp import DoesApartments
            # Question 3
from oopp import HumanResource
            # Question 4 & 5
from oopp import JamesBookStore

'''
Question 7 :

* What is the difference between an instance method,
  a class method and a Static method?
  
*****************************************************

Instance method:

	Instances has self as a parameter (used the most)

Class method: (rarely used)

	Defined by @classmethod

	it is a method that has a class object(instead of self)
	cls is similar of to self. The main difference is self
	refers to an instance, while cls refers to a class.

	We can use it to access our class variable.


Static method:

	Static method is a method that is not passed an
	instance or a class it neither has self or cls as the 
	first parameter- To call the method,

	We can either  call it by the class name or the instance
	name.

********************************************************

  * In the code below, which is an instance method 
  and which is a class method?

  class MethodsDemo:
  	message = 'Class message'

  	def __init__(self, pMessage): // Instance
  		self.message = pMessage

  @class method // Class method
  def printMessage(cls):
  	print(cls.message)

  def printAnot herMessage(self):
  	print(self.Message)

 *** Given that md1 = MethodsDemo('md1 Instance Message'),
 what are the two ways to call the class method?

Method 1
 // MethodDemo().ClassM()

Method 2:
	# Add methodDemo() into a variable
mDemo = MethodDemo()
 // Calling the class method
mDemo.classM()

 **** Add a static method called printThirdMessage()
 	  to the MethodsDemo class that simply prints the message 
 	  "This is a static method".

****** What are the two ways to call the static
	   method in part *****?
'''
class MethodsDemo:
        message = 'Class message'

        def __init__(self, pMessage): # Instance
           self.message = pMessage
           print("Instance created")

        @classmethod# Class method
        @staticmethod # Static method

        def klasse(cls): # Class method
            print(cls.message)

        def instanceM(self): # Instances  method
            print(self.Message)

        def Static(message = 'static'): # Static method
            print(message)
            
instance = MethodsDemo('This is a instance')
method.klasse()
method.Static()

            # // Question 8
from klasse import ChinemaMovies