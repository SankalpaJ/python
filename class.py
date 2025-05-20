# class Employee:
#     name = "Sankalpa J"
#     age = 22         # variable directly presented inside class "class level variables" (name ,age)..
#     def study(self):       # instance method
#         print("Employee is  Studying...")
# e1 = Employee()
# e2 = Employee()
# print(e1.name)  # go inside d e1(obj) & get value from Employee cls..
# print(e2.age)
# e1.study()  
# e2.study()
'''
Sankalpa J
22
Employee is  Studying...
Employee is  Studying...
'''

# class User:
#     bank_name = "SBI"
#     def deposit(self):
#         print("Deposit Method")
#     def withdraw(self):
#         print()
# u1 = User()
# u1.name = "Sankalpa"  # go inside u1 & initialize name to it..
# u1.Accno = 4202      # instance varibale...
# u1.bank_name

# u2 = User()        # has part(name, AccNo)
# u2.name = "Adiii"
# u2.AccNo = 4023


# class Employee:
#     company_name = "Code"
#     def work(self):
#         print(self.name,"z working...")
#     def play(self):
#         print(self.name,"z playing..")
# e1 = Employee()
# e1.name = "Sankalpa"
# e1.id = 101
# e1.work()

# e2 = Employee()
# e2.name = "Sumith"
# e2.id = 102
# e2.work()
# e2.play()
'''
Sankalpa z working...
Sumith z working...
Sumith z playing.. 
'''

# -------------------------------------------------------------
'''
1. 'Instance (obj) Methods':-- The Methods which are present inside d clss are called 'Instance (obj) Methods'...
2. For this methods self parameter z must.. bcz python needs it..
3. 'Instance (obj) varibale':-- variable present inside an 'object' z called 'Instance varibale' seprate copy z ceated for each obj or instances(u1 & u2)..
4. bank_name = "SBI" => class level variable (bcz it z common for all objs..)
5. 'class level variable':-- variable created directly inside  d  class..
6. 'local variables': var created inside d stack frame in memory
7. self parameter:--- 'self' is  like 'this' keyword in Java
8. always 'self' holds d adress of current obj...
'''