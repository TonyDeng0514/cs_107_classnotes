class Student:
   Total= 0
   def __init__(self, name="Adam", id="123456789"): # default informations
       self.name = name # property of self
       self.ID = id     # property of self
       Student.Total += 1
   def displayCount(self):  # 
       print ("Total students %d" % Student.Total)
   def displayStudentDetails(self):
       print ("Name: ", self.name, ", ID: ", self.ID)

         
'''
This code is building three things, adam, alice, bob.
'''


if __name__ == "__main__":
    Student1 = Student()
    Student1.displayStudentDetails()
    Student1.displayCount()

    Student2 = Student("Alice", 23456789876)
    Student2.displayStudentDetails()
    Student2.displayCount()
   
    Student3 = Student(id=23456789876, name="Bob")
    Student3.displayStudentDetails()
    Student3.displayCount()
