class Employee:
# creating constructor of EMmployee cls using( __init__())
    def __init__(self): 
        self.emp_name = "AK"   # instance varaibles name & id
        self.emp_id = 101      # static value..
# creating obj
e1 = Employee()
# Accessing properties of e1 obj:
print('Employee name for e1 is:', e1.emp_name)  # Employee name is: AK
print('Employee id for e1 is:',e1.emp_id)       # Employee id is: 101

# creating obj
e2 = Employee()
# Accessing properties of e1 obj:
print('Employee name for e2 is:', e2.emp_name) 
print('Employee id for e2 is:',e2.emp_id) 

'''
Employee name for e1 is: AK
Employee id for e1 is: 101
Employee name for e2 is: AK
Employee id for e2 is: 101

here for both e1 & e2 we are  getting same name & id's,,
it means duplicate values think of creating instagram a/c &
getting all username & id as like this.. To fix it refer Const1.py.......
'''
