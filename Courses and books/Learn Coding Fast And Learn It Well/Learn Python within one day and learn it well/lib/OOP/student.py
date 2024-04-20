
'''
Question 4

Create a class called Student.

The class has 4 instance variable: name, id, course_enrolled and annual_fees.
Within the class, we need to have an __init__method to initialize the 4 instance variables.
We also need to have a __str__ method.

Code the class your self.

Next we inherit three subclasses from Student. The first subclass is ArtStudent.
It has a additional instance variable called pProjectGrade

The second subclass is CommerenceStudent. It has an additional variable called
internship_company.

The third subclass is TechStudent. It has two additional instance variables called
internship_company and project_grade.

Least but not least, we need to add the __It__ and __gt__ methods to our parent class.
These are special methods in Python that allow us to make comparison.

LT stands for "less than" while GT stands for "greater than". They override the < and >
operators respectively.

Add these two methods to the Student class so that they allow us to compar the annual fees
(sstored in the instance variable annual_fees) of two instances and return True or False
accordingly. For instance, if we have the follwoing code :


student1 = Student('jim', 'A19001', 'Psychology', 12000, 'In Progress')

student2 = CommerceStuden('Ben', 'C19011', 'Marketing', 15000, 'Cool Mart)

student1 > student2 should give us False as the annual_fees of student1 is lower than that
of student2

In contrast, student1 < student2 should give us True.

Once that is done, save the file as student.py on your desktop.
Next, create another file called ch10q4.py on your desktop and import the classes in student.py

Instantiate three instances with the following information and print a string representation
of each instances :


'''

class Student:
    def __init__(self, pName, pId, pCourse, pFee):
        self.name = pName
        self.id = pId
        self.course = pCourse
        self.fee = pFee
        print("Student", self.name, "Created !")
        
    def __str__(self):
        return '\nStudent Info of %s (id: %s).\n Course : %s,\n Annualfee : %d $.\n Project Grade : %s' % (self.name, self.id, self.course, self.fee,)

    def __lt__(self, pOther):
        self.another = pOther
        
        if self.fee < self.another.fee:
            print(" The annual fees of %s is lower than %s" % (self.name, self.another.name))
        else:
            print("The annual fees of %s is greater than %s" % (self.name, self.another.name))
        
    def __gt__(self, pOther):
        self.another = pOther
        
        if self.fee > self.another.fee:
            print(" The annual fees of %s is greater than %s" %(self.name, self.another.name))
        else:
            print("The annual fees of %s is lower than %s" % (self.name, self.another.name))
            
class ArtStudent(Student):
    def __init__(self, pName, pId, pCourse, pFee,pProjectGrade):
        self.id = pId
        self.fee = pFee
        self.name = pName
        self.course = pCourse
        self.pgrade = pProjectGrade
        
    def __str__(self):
        return '\nStudent Info of %s (id: %s).\n Course : %s,\n Annualfee : %d $.\n Project Grade : %s' % (self.name, self.id, self.course, self.fee, self.pgrade)

class ComStudent(Student):
    def __init__(self, pName, pId, pCourse, pFee, pInternshipCompany):
        self.id = pId
        self.fee = pFee
        self.name = pName
        self.course = pCourse
        self.internComp = pInternshipCompany

    def __str__(self):
        return '\nStudent Info of %s (id: %s).\n Course : %s,\n Annualfee : %d $.\n Intern Company : %s' % (self.name, self.id, self.course, self.fee, self.internComp)


class TechStudent(Student):
    def __init__(self, pName, pId, pCourse, pFee, pInternshipCompany, pProjectGrade):
        self.id = pId
        self.fee = pFee
        self.name = pName
        self.course = pCourse
        self.pgrade = pProjectGrade
        self.internComp = pInternshipCompany
    def __str__(self):
        return '\nStudent Info of %s (id: %s).\n Course : %s,\n Annualfee : %d $.\n Project Grade : %s \n Internship Company : %s' % (self.name, self.id, self.course, self.fee, self.pgrade, self.internComp)
st1 = ArtStudent('Jhon Doe', 'A19001', 'Psychology', 12000, 'in Progress')
st2 = ComStudent('Jane Doe', 'C19011', 'Marketing', 15000, ' Cool Mart')
st3 = TechStudent('Martin Doe', 'B29011', 'Python', 10000,' Prostaff', 'Calculating.. ' )
print(st1, "\n", st2, "\n", st3, "\n")
print(st1 < st2)

