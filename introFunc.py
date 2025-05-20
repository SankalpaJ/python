# func z a set of instructions which can be reused again and again...
# syntax: (func_name, func_body, parametrs, arguments, calling_fun)..
# ex: def add(a,b)  -- method declartion & a,b are parameters....
#         print("") -- body
#      add(10,20)        -- calling & 10, 20 are arguments....

# def add(a,b):
#     print("Inside add method..")  # Inside add method..
#     print("Addition is:", a+b)   # Addition is: 30
# add(10,20)

# types:---
# 1. funs w/o parameters and return statement..
# def add():
#     a = 10
#     b = 20
#     c = 30
#     print("Sum is: ", a+b+c)
# add()                           # Sum is: 60

# 2. funs w/o parameters & with return statment..
# def add(a,b):
#     return a+b
# res = add(10,20)
# print(res)       # 30

# 3. funs with parameters & w/o return..
def add(a,b):
    print("Sum is:", a+b)
add(100,20)     # Sum is: 120

# 4. funs with parameters & with return...

