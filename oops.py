# Oops:- z d way of solveing prlm by wrting cls & obj
# Ex:
# class Employee:
#     name = 'Akil'
#     age = 23          # has part
#     def eat(self):     # does part & 'self' word or any name parameter(s, a, b etc) z  must whenevr we defining function inside class.....
#         print("Emplyee is Eating...")

# classes will not require/occupy memory but obj wt we created for cls will require memory...
# creation of class
class Student:
    # roll = 123
    # marks = 79
    def study(self):
        print("Study Method...")
    def eat(self):
        print("Eating method...")
# object creation :- it z alwys created in 'heap segment' & reference variable (s1) will present in 'stack segmt'...
s1 = Student()
s2 = Student()
