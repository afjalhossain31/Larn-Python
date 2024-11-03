# Create constructor function
class Student:
    Roll = " "
    CGPA = " "

    def __init__(self, Roll, CGPA):
        self.Roll = Roll
        self.CGPA = CGPA

    def display(self):
        print(f"Roll :{self.Roll}, CGPA :{self.CGPA}")


object = Student(2002, 3.50)
object.display()

object2 = Student(2323, 3.65)
object2.display()
