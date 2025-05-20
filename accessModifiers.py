''' 1) public varible:        name
    2) protected variable:   _name
    3) private variable:    __name
'''
# class Demo:
#     def __init__(self):
#         self.name = "Sankalpa"
#     def disp(self):
#         print(self.name)  # accessing public propety inside same cls
# d1 = Demo()
# print(d1.name)    # accessing public property outside d cls -- Allowed

# class Demo1(Demo):
#     def disp(self):
#         print(self.name)  # accessing public property inside child cls -- Allowed
# dm1 = Demo1()
# dm1.disp()

# class Code:
#     def display(self):
#         print(d1.name) # access public property inside non-childl cls -- allowed
# c = Code()
# c.display() 
'''
Sankalpa
Sankalpa
Sankalpa  
'''
# -----------------------------------------------------------------------------------------------------
# protected:-- d protected variable must beaccessed inside d same cls or inside child cls...
# class Demo1:
#     def __init__(self):
#         self._name = "SA"    # protected variable
#     def disp1(self):
#         print(self._name)    # accessing inside d same cls
# d1 = Demo1() 

# class Demo2:
#     def disp(self):
#         print(self._name)    # accessing inside d child cls
# d2 = Demo2()

# ------------------------------------------------------------------------------------------
# private:--- must be accessed inside d  same cls
class Demo1:
    def __init__(self):
        self.__name = "SA"      # private var
    def disp1(self):
        print(self.__name)
d1 = Demo1()
# print(d1.__name) # error so use "Name mangling" (_clsName__varName) as follow..
print("Accessing private var outside d cls: ", d1._Demo1__name)    # Accessing private var outside d cls:  SA
'''
Name mangling:-- is d process of giving new name to private var in format of:-- 
                   (_clsName__varName)  by this we can access it outside d cls..
'''
# -------------------------------------------------------------------------------------------------------------------
'''
Access Modifier ae used to determine d accessibility of methods & properties. 
1) public: When we want to access variables anywhere in the code.
2) protected: When we want to access variables inside the same class and inside child class.
3) private: When we want to access variables inside the "same class". its like cls-level variable

    "public & protected" will act same but its developer duty to define as per rules..
python won't support "protected" access modifier its just a  msg from developer to develpoer to access
     d var as per thier accessability given in code.
    

public: a = 10
protected: _a = 10
private: __a = 10
'''

# k-app prm
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary  # Private attribute

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print(f"Salary updated to {self.__salary}.")
        else:
            print("Invalid salary amount. Salary must be greater than 0.")

    def get_salary(self):
        return self.__salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.employee_id}")


# Taking input from the user
name = input()
employee_id = input()
initial_salary = int(input())
new_salary = int(input())

# Creating an instance of Employee
employee = Employee(name, employee_id, initial_salary)

# Displaying employee information
employee.display_info()

# Updating salary
employee.set_salary(new_salary)

# Displaying updated salary
print(f"Current Salary: {employee.get_salary()}")


