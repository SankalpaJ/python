# bool()
# print(bool(12))   # True -- int to bool
# print(bool(12.346))  # True -- float to bool
# print(bool('Code'))  # True -- string holding string to bool
# print(bool(0))       # False -- int to bool
# print(bool(''))      # False -- empty string to bool

# float() 
# print(float(123)) # 123.0 -- int to float conversion
# print(float('code')) # Error -- string holding string to float
# print(float('123.34')) # 123.34 -- string holding float to float
# print(float(True))  # 1.0 -- bool to float
# print(float(False)) # 0.0 

# int()
# print(int('123.345')) # Error -- string holding float to int
# print(int('code'))  # Error -- string holding string to int
# print(int(True))  # 1 -- bool to int
# print(int(False)) # 0 
# print(int('123')) # 123 -- string holding int to int allowed
# print(int(123.46)) # 123 -- float to int conversion

# https://github.com/Priya9096/Python-Codes-2025-

'''we can't convert string to int but if string containing int value then it can be converted to int in python.... '''

num1 = int(input("Enter num1  :")) #10
num2 = int(input("Enter num2  :")) #2
print(num1/num2 ,type(num1/num2))  #5.0 <class 'float'>

# Whenever we are performing division operation the result will always be in float.

