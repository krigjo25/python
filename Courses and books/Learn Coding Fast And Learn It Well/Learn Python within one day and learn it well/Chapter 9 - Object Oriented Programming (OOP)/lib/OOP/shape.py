
'''
Chapter 10 Object Oriented Programming Part 2

Question 1

Create a file called shape.py and save it onto your desktop. Add the following code
to the file:

class Shape:
    def __init__(self, pType, pArea):
        self.type = pType
        self.area = pArea

    def __str__(self):
    return '%s of area, %4.2f unit square' %(self.type, self.area)

class Square(Shape):
    def __init__(self, pLength)
    super().__init__('Square',0)
    self.length = pLength
    self.area = self.length * self.length

The code above consist of two classes - Shape and Square.

Square is a subclass that inherits from Shape. This subclass only has one instance
__init__, with two parameters self and Length.

Within the method, we first call the __init__ method from the parent  class
(using the super() function), passing in 'Square and 0 as arguments.

These arguments are used to initialized the instance variables type and area in the parent
class, which the subclass inherits.

Next we assign the parameter pLength to a new instance variable called length. In addition,
we calculate the area of a square and use it to update the value of the inherited instance
variable area.

( Note :
The area of a square is given by the square of its length).

Study the code above and make sure you fully understand it.


Next, we need to add two more subclasses, Triangle and Circle, to shape.py.
Both subclasses have one method: __init__.

You need to decide on the appropriate parameter(s) for these methods.

Both __init__ methods should call the __init__ method in the parent class and pass in
appropriate values for the inherited instance variable type and area.

In addition, they should have their own instance variable and contain a statement for
updating the value of the inherited instance variable area.

Try modifying the Square subclass your self to code the Triange and Circle subclasses.


Hint :

    Triangle is defined by its base and height and its area is given by the mathematical
    formula :  0.5*base*height.

    A Circle is defined by its radius and its area is given by mathematical formula :
        Pi*r*r

    pi is a constant represented as math.pi in the math module. You need to import the math
    module to get the value of pi.
'''

'''
Question 10.2

In this question, we shall modify the Shape class in Question 1 by adding one more method
to it - the __add__ method.

This method has two parameters, self and other, and overrides the + operator. instead of
performing basic addition, the + operator should return the sum of the areas of two Shape
Instances. In other words, if one instance has an area of 11.1 and another has an area of
7.15, the __add__ method should return the value of 18.24.

Add the __add__ method to the Shape class in shape.py.

Next, use the print() function in shapemain.py to verify that sq + c gives you the sum of
areas of sq and c.
'''
import math

class Shape:
    def __init__(self, pType, pUnit, pArea):
        self.type = pType
        self.unit = pUnit
        self.area = pArea
        print ("Class", self.type, "Created")

    def __str__(self): # Attribute
        
        return 'The %s of a %s is : %4.2f' %(self.unit, self.type, self.area)
    
    #  shape + shape
    def __add__(self, pOther): # Addition for two shapes
        self.another = pOther
        sum = self.area + self.another.area
        return Shape('Total values ', self.unit, sum)
    
        
        
        
        
# Inherits from the parent class
class Square(Shape):
    def __init__(self, pLength):
        super().__init__('Square', 'Length', 0) # Inherits from primary class pType and pArea
        self.length = pLength
        self.area = self.length ** 2



class Triangle(Shape):
    def __init__(self, pBase, pHeight):
        super().__init__('Triangle','Area', 0)
        self.base = pBase
        self.height = pHeight
        self.area = 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self,pRadius):
        super().__init__('Circle','Radius', 0)
        self.radius = pRadius
        self.area = self.radius ** 2 * math.pi
        

