'''
1) polymorphism: Something which is showing many forms..
   ex:  '+' --> used to perform 'addition' & also used for 'String concatination'..
2) ex:-- i) Method Overloading :-- process of crating multiple methods with same name but "different parameters"..
        ii) Method Overidding :-- 
       iii) Operator Overloading:-- 1 method performing multiple tasks..
        iv) Duck Typing:-- we keep accepting obj w/o cheching type of obj..
'''

# i) Method Overloading :-- python will also not suport method Overloading like JS..
# always last declered function will be called...
def disp():
    print("Inside disp with 0 parameters")
def disp(a):  
    print("Inside disp with 1 parameters")
def disp(a, b):
    print("Inside disp with 2 parameters")
def disp(a, b, c):
    print("Inside disp with 3 parameters")
# disp()   # TypeError: disp() missing 3 required positional arguments: 'a', 'b', and 'c'
# disp(10)   # TypeError: disp() missing 2 required positional arguments: 'b' and 'c'
# disp(10, 20)  # TypeError: disp() missing 1 required positional argument: 'c'
disp(10, 20, 30)  # Inside disp with 3 parameters

# -----------------------------------------------------------------------------------------------------------------


# ii) Method Overidding:-- 
class Parent:
    def cook(self):
        print("Cooking puri & saagu.")
    def learn(self):
        print("Learing how to cook by watching in u-tube.")
class Child(Parent):
    def play(self):
        print("Playing Cricket..")
    def learn(self):
        print("Learning Python by watching kodnest..")
c = Child()
c.cook()   # Cooking puri & saagu.

'''
1) Inherited Method:-- d method which z deriverd from parent cls & used as it z in child cls..
    ex:-- cook()
2) Specialized Method:-- method which z only avaiable for child cls & not for parent cls (child-specific)..
     ex:-- play()
3) Overidden Method:-- methods deriverd from parent cls & modified into child cls as per child cls requirement..
     ex:-- learn()
'''
# -----------------------------------------------------------------------------------------------------------------

#  iii) Operator Overloading:--
'''
Magic methods/ dunder methods: method which has suffic & prefix as "double underscore"..
i) __init__():-- called automatically, while creating an object to initialize "instance var"..
ii) __str__():-- called when we are trying to printn object reference..
'''

class Student:
    def __init__(self, name):
        self.name = name
    def learn(self):
        print(self.learn, "is Learing")
s1 = Student("Pooja")
print(s1)  # Obj Reference:-- <__main__.Student object at 0x000001E98DEF6BA0>   

'''
whenever we try to print obj of cls d python internally calls d "__str__()"
  so, that it always return String reprentation of adress of an obj, as o/p as above.. 
To return which we want as o/p use __str__() as follows..

-> when we are trying print obj reference then __str__() will be called..
-> d internal __str__() will always retrun "String representation of an address"...
'''

class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __add__(self, other):  
        return self.name + other.name
    def __sub__(self, other):
        return self.name + other.name
    def __mul__(self, other):
        return self.name + other.name
    def __truediv__(self, other):    # __truediv__ or __floordiv__
        return self.name + other.name
s1 = Student("Pooja")
print(s1)  # Pooja

s2 = Student("Akash")
print(s2)  # Akash
 
print(s1 + s2)  # PoojaAkash
print(s1 - s2)  # PoojaAkash
print(s1 * s2)  # PoojaAkash
print(s1 / s2)  # PoojaAkash

# -----------------------------------------------------------------------------------------------------------------

# iv) Duck Typing:-- If something walking like a duck, qucks like duck then it z duck..
'''
 --> here it will not see "has part" it only see "does part" of obj & d obj can be anything...
 -->   ex:-- Dog --> walking like a duck, qucks like duck -- Dog z Duck..
 --> we can reduce typing of code again & agian as following..
 --> Remove code redudency..
 --> we won't acre about type of obj we only care behaviour of obj..
'''

class Add():
    def calculate(self, a, b):
        print(a + b)
    
class Mul(): 
    def calculate(self, a, b):
        print(a * b)

class Div():
    def calculate(self, a, b):
        print(a / b)

# ref = Mul()
# ref.calculate(10, 20)

# ref = Add()
# ref.calculate(5, 10)

# ref = Mul()
# ref.calculate(2, 5)

# ref = Div()
# ref.calculate(10, 2)  # here again & again type of "ref.calculate(10, 2)"

# duck typing: to remove code redundnecy
def permit(ref):
    ref.calculate(10, 20)
permit(Add())   # 30
permit(Mul())   # 200
permit(Div())   # 0.5
# creating 1 ref for multiple objets of 3 d/f cls
# 1stly we are creating 1 1 sepreate obj for each cls now by using "duck typing" we creating like thiss...


 








