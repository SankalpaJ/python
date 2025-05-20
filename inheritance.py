'''
# types:
1. Single inheritance:-- One cls inherits from another....
2. herierchal inheritance:-- Multiple clss inherits from d "Same base cls"....
3. Multiple :-- A cls inherits from more than 1 base cls...
            Java doesn't support but Pyhton supports it using MRO technique..
4. Multi-level:-- A chain of clss hwere each cls inherits from 1 above it.....
5. Hybrid:;--     A mix of different  inheritance types...

'''
# 1. single inheritance
class Demo1:
    def disp1(self):
        print("disp1")

class Demo2(Demo1):
    def disp2(self):
        print("disp2")
# to access both demo1 & demo2
d2 = Demo2()
d2.disp2()
d2.disp1()
'''
disp2
disp1
'''

# 2.herierchal inheritance
class Demo1:
    def disp1(self):
        print("disp1")
class Demo2(Demo1):
    def disp2(self):
        print("disp2")
class Demo3(Demo1):
    def disp3(self):
        print("disp3")
d3 = Demo3()
d3.disp1()
d2 = Demo2()
d2.disp1()
'''
disp1
disp1
'''
# 3.Multi-level
class Demo1:
    def disp1(self):
        print("disp1")
class Demo2(Demo1):
    def disp2(self):
        print("disp2")
class Demo3(Demo2):
    def disp3(self):
        print("disp3")
d3 = Demo3()
d3.disp3()
d3.disp2()
d3.disp1()
'''
disp3
disp2
disp1
'''
# 4.multiple inheritance :- MRO [Method Resolution Order]
# it defines d order in which mthods are searched in a multiple inheritance scenario...

class Demo1:
    def disp1(self):
        print("Inside disp1")
class Demo2:
    def disp2(self):
        print("Inside disp2")
class Demo3(Demo1, Demo2):
    def disp3(self):
        print("Inside disp3")
d3 = Demo3()  # instance var doesn't contain 'constructor'
d3.disp3()
d3.disp2()
d3.disp1()
'''
Inside disp3
Inside disp2
Inside disp1

MRO:--- disp3 ---> Demo3
        disp2 ---> Demo3 ---> Demo1 ---> Demo2
        disp1 ---> Demo3 ---> Demo1
''' 

# another ex for MRO
# class Demo1:
#     def magic(self):
#         print("Inside magic of Demo1")
# class Demo2:
#     def magic(self):
#         print("Inside magic of demo2")
# class Demo3(Demo1, Demo2):
#     pass
# d3 = Demo3()
# d3.magic()  
# print(Demo3.__mro__) # to see which sequence d code execting
'''
Inside magic of Demo1
(<class '__main__.Demo3'>, <class '__main__.Demo1'>, <class '__main__.Demo2'>, <class 'object'>)
'''

# MRO using constructor...
# class Demo1:
#     def __init__(self):
#         self.x = 100
# class Demo2:
#     def __init__(self):
#         self.x = 200       # here if we remove this line & give "pass" it still provde same res...
# class Demo3(Demo1, Demo2): # Demo3(Demo2, Demo1)    res--- 200
#     pass
# d3 = Demo3()  # caling of constructor
# print(d3.x)    # 100

'''
__init__ Demo3 --> Demo1
'''

# Super Method --> super() this will call next cls constructor as per MRO
# class Demo1:
#     def __init__(self):
#         self.x = 100
# class Demo2:
#     def __init__(self):
#         self.x = 200
#         super().__init__()
# class Demo3(Demo2, Demo1):
#     pass
# d3 = Demo3()
# print(d3.x)     # 100
'''
Demo3 --> Demo2 --> Demo1 --> obj
'''

# nxt exp:---
class Demo1:
    def __init__(self):
        self.x = 100
        super().__init__()
class Demo2:
    def __init__(self):
        self.x = 200
        super().__init__()
class Demo3(Demo1, Demo2):
    pass
d3 = Demo3()
print(d3.x)     # 200
'''
Demo3 --> Demo1 --> super() Demo2 --> obj
'''
