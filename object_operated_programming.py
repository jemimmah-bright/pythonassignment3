# creating a class in OOP
#syntax
#its key to start the class names with upper case and singular


# add a constracter for the corhot class
# add a method to the calss that prints the corhot name and the total number of students
#create a new object of the corhot class

# OOP(Object Oriented Programming)
 # It has priciples like classses,objects.
#a class always has properties/ attributes
# An object comes from the class.


    #assignment
#1. Add a constructor for the cohort class

#2. Add a method to the class that prints the cohort name
# and the total number of students

#3. Create a new instance of the cohort class
 
#OOP
#Object Oriented Programming is a style of programming characterized by the 
# identification of classes or objects closely linked with methods (functions)with which they are associated with.

#CLASSES.
#Class is a template/object constructor for creating objects.
#All classes _init_() function which is always executed when the class is being initiated.

#OBJECTS/INSTANCE.
#Instance is an object that belongs to a class. 

# number one
class cohort_four:
    def _init_(self, student_name,start_date,course_units,course):
        self.student_name = student_name
        self.start_date = start_date
        self.course_units = course_units
        self.course = course
cohort4 = cohort_four("Bright", "23/12/2024", "seven course units","Computer Science")
print("The student name is: ", cohort4.student_name)
print("Th start date is : ",cohort4.start_date)
print("The course units are: ",cohort4.course_units)
print("The course name is : ",cohort4.course,'\n')

#number two
#2. Add a method to the class that prints the cohort name
# and the total number of students

class cohort:
  def _init_(self, cohort_name, number_of_students):
    self.cohort_name = cohort_name
    self.number_of_students = number_of_students

  def myfunc(self):
    print("\nThe cohort name is " + self.cohort_name + " and the number of students in the cohort is " + str(self.number_of_students),'\n\n' )

cohort_details = cohort("Cohort four", 60)
cohort_details.myfunc()

#3. Create a new instance of the cohort class
# The new instance for the cohort four class is cohort five
class CohortFour:
    def _init_(self, student_name, start_date, course_units, course):
        self.student_name = student_name
        self.start_date = start_date
        self.course_units = course_units
        self.course = course

cohort_five = CohortFour("Jemimmah Sanyu", "12/01/2025", "eight course units", "Computer Science")# Creating a new instance of the CohortFour class

# Printing the details of the new cohort instance cohort_five
print("\nThe student name is:", cohort_five.student_name)
print("The Start Date for cohort5 is :", cohort_five.start_date)
print("The Course Units are:", cohort_five.course_units)
print("The course is :", cohort_five.course,'\n\n')