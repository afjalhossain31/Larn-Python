# create method and function
class Student:
    roll = ""
    cgpa = ""

    # create method and function
    def set_value(self, roll, cgpa):
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Roll :{rahim.roll}, GPA :{rahim.cgpa}")


rahim = Student()
rahim.set_value(1730, 3.50)
rahim.display()


karim = Student()
karim.set_value(1422, 4.88)
karim.display()


"""
class Student:
    roll = ""
    cgpa = ""
    def display(self):
      print(f"Roll :{rahim.roll}, GPA :{rahim.cgpa}")
      
rahim=Student()
rahim.roll=292 
rahim.cgpa=3.43
rahim.display()

karim=Student()
karim.roll=292 
karim.cgpa=3.43
karim.display()
   
        
"""
