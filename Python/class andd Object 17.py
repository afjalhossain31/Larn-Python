# this is a templete function
class Student:
    roll = ""
    gpa = ""


# Student class er object rahim
rahim = Student()
print(isinstance(rahim, Student))
rahim.roll = 101
rahim.gpa = 3.50

print(f"Roll :{rahim.roll}, GPA :{rahim.gpa}")

# Student class er object karim
karim = Student()
print(isinstance(rahim, Student))
karim.roll = 102
karim.gpa = 4.00

print(f"Roll :{karim.roll}, GPA :{karim.gpa}")
