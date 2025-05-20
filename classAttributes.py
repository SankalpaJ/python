class Emp:
    college_name = 'BIET'    # cls-level var
    def __init__(self,name):
        self.name = name

e1 = Emp('Akash')
e2 = Emp('Akith') # instance var e1 & e2

# Accessing cls-level var using obj reference or cls_name
print(e1.college_name)   # BIET
print(e2.college_name)    # BIET
print(Emp.college_name)    # BIET

'''
class v/s Instance Variables:---

1. cls-level var are such variables which are declared inside d cls &
         outside any method...
2. All objects for that cls share same copy of cls var.. (like clg_name)

1. Inc var are such var present inside d obj
'''