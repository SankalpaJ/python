# class Student:
#     def __init__(self, name, id):
#         self.st_name = name
#         self.st_id = id
#     def learn(self):         # does part----
#         print(self.st_name,"Learning...")
#     def play(self):
#         print(self.st_name,"Playing...")  # does part ----

# s1 = Student('AK', 101)
# s2 = Student('PK', 102)
# print("Student name of s1 is: ", s1.st_name)
# print("Student id for s1 is: ", s1.st_id)
# s1.learn()
# s1.play()
# print("Student name of s2 is: ", s2.st_name)
# print("Student id for s2 is: ", s2.st_id)
# s2.learn()
# s2.play()
'''
Student name of s1 is:  AK
Student id for s1 is:  101
AK Learning...
AK Playing...
Student name of s2 is:  PK
Student id for s2 is:  102
PK Learning...
PK Playing...

here code  redudancy will be their so see below code...
'''

# class Student:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def learn(self):
#         print(self.name,'is Learning')
#     def play(self):
#         print(self.name,'is Playing')
#     def displayInfo(self):
#         print('Student Details: ')
#         print('Student Name is:',self.name)
#         print('Student ID is:',self.id)
# s1 = Student('Ranjith',101)
# s2 = Student('Pranva',102)
# #Access Methods for s1:
# s1.learn()
# s1.play()
# s1.displayInfo()
# #Access Methods for s2:
# s2.play()
# s2.displayInfo()

'''
Ranjith is Learning
Ranjith is Playing
Student Details:
Student Name is: Ranjith
Student ID is: 101
Pranva is Playing
Student Details:
Student Name is: Pranva
Student ID is: 102

here static or hard coded values are provided to take user input refer below code...
'''
# Vechicle rental s/m using some conditions..
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.is_available = False
    def display_info(self):
        status = 'Rented' if self.is_available else 'Available'
        print(f"Make: {self.make}, Model: {self.model}, Status: {status}")
    def mark_rented(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.make} {self.model} has been marked as rented.")
v1 = Vehicle('Honda','Civic')
v1.display_info()
v1.mark_rented()
v1.display_info()
'''
Make: Honda, Model: Civic, Status: Available
Honda Civic has been marked as rented.   
Make: Honda, Model: Civic, Status: Rented
'''

# taking user input Online Store Product Management...
name = input("Enter a name: ")
price = float(input("Enter a price: "))
stock = int(input("Enter a no of stock: "))
new_price = int(input("Enter a  new_Price: "))
new_stock = int(input("Enter a  new_Stock: "))
# creating class 
class Product:
# creating constructor
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def display_info(self):
        print(f"Product Name: {self.name}, Price: {self.price}, Stock: {self.stock}")
    def updated_price(self, new_price):
        self.price = new_price
        print(f"Updating Price to {new_price}... \nNew Price: {self.price}")
    def updated_stock(self, new_stock):
        self.stock = new_stock
        print(f"Updating stock to {new_stock}... \nNew Stock: {self.stock}")
# creating obj & passing values to it
p1 = Product(name, price, stock)
p1.display_info()
p1.updated_price(new_price)
p1.updated_stock(new_stock)
'''
Enter a name: Laptop
Enter a price: 1000.0
Enter a no of stock: 20
Enter a new_Price: 1500
Enter a new_Stock: 15

Product Name: Laptop, Price: 1000.0, Stock: 20
Updating Price to 1500...
New Price: 1500
Updating stock to 15...
New Stock: 15
'''





