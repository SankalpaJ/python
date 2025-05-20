class Employee:
    def __init__(self,name,id):
        self.emp_name = name
        self.emp_id = id
# creating obj: (dynamically assigning value..)
e1 = Employee('Pinky', 101)  # calling of constructor of emp cls & as soon obj will be created...
e2 = Employee('Sinku', 102)

#Accessing Properties of e1 obj:
print('Employee name of e1 is: ', e1.emp_name)
print('Employee id  for e1 is: ', e1.emp_id)

#Accessing Properties of e2 obj:
print('Employee name of e2 is: ', e2.emp_name)
print('Employee id  for e2 is: ', e2.emp_id)

'''
Employee name of e1 is:  Pinky
Employee id  for e1 is:  101
Employee name of e2 is:  Sinku
Employee id  for e2 is:  102

name & id => local variables..   
'''