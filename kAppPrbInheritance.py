# Single inheritance:--
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age) # calling d constructor of base cls..
        self.id = id
    def display_emp_details(self):
        self.display_person_info()
        print(f"Employee ID: {self.id}")

name = input("Enter a name: ")
age = input("Enter age: ")
id = input("Enter id: ")
e1 = Employee(name, age, id)
e1.display_emp_details()
'''
Enter a name: Sankalpa J
Enter age: 22
Enter id: E12345
Name: Sankalpa J
Age: 22
Employee ID: E12345
'''

# Multiple Inheritance:-- 
class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_device_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
class Warranty:
    def __init__(self, warranty_provider, warranty_expiry):
        self.warranty_provider = warranty_provider
        self.warranty_expiry = warranty_expiry
    def display_warranty_details(self):
        print(f"Warranty Provider: {self.warranty_provider}")
        print(f"Warranty Expiry: {self.warranty_expiry}")
class Laptop(ElectronicDevice, Warranty):
    def __init__(self, brand, model, sel_no, warranty_provider, warranty_expiry):
        ElectronicDevice.__init__(self,brand,model)   # call d constructor 
        Warranty.__init__(self,warranty_provider, warranty_expiry)  # call d constructor 
        self.sel_no = sel_no
    def display_laptop_info(self):
        self.display_device_info()   # calling of base cls method
        print(f"Serial Number: {self.sel_no}")
        self.display_warranty_details()
brand = input("Enter d brand: ")
model = input("Enter d model: ")
sel_no = input("Enter d serial number: ")
warr_pro = input("Enter d Warranty Provider: ")
warr_exp = input("Enter d Warranty Expiry: ")
l1 = Laptop(brand, model, sel_no, warr_pro, warr_exp)
l1.display_laptop_info()
'''
Enter d brand: Apple
Enter d model: MacBook Air
Enter d serial number: S1234
Enter d Warranty Provider: AppleCare
Enter d Warranty Expiry: 2025-07-12
Brand: Apple
Model: MacBook Air
Serial Number: S1234
Warranty Provider: AppleCare
Warranty Expiry: 2025-07-12
'''
