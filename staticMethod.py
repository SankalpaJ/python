class MathOperar:
    @staticmethod
    def add(a,b):   # not used 'self' bcz we not called used any obj reference
        print(a + b)
    def sub(self, a, b): # instance  method bcz using 'self' word
        print(a - b)
# invoking static method
MathOperar.add(10, 20)    # 30

m1 = MathOperar()         # -100
m1.sub(200,300)

''' 
Instance Methods v/s Static Methods:---

1. use '@staticmethod' decorator (adding extra funcs) for definig static method [cls-level Methods]
2. accessed using either 'cls_name' or 'obj_ref' & don't  use 'self' word..
2. instance method we must define with refernce var
'''