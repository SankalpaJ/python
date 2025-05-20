# converting 1 type of data into another type...
# when ever we try to convert data to another automatically data type will be changed..

# int():
# a = '10'
# print(a, type(a))  # 10 <class 'str'>
# b = int(a)
# print(b, type(b))   # 10 <class 'int'>

# print(int('100'))  # converting string('100') to int...
# print(int('123.22')) # Error  only when string containg int can covert
# print(int('100'))  # like this
# print(int('code'))  # Error
# print(int(True))   # 1   converting int to boolean..

# str(int) -> int   YES
# str(float) -> int  No (Error)
# str(str) -> int    No  (Error)
# str(bool) -> int  No  str('True')

# print(int('12'))
# print(int('code'))  # Error
# print(int('12.44')) # Error
# print(int('True'))    # Error
 
# WAC to take 2 float num from from user & display its addition
# num1 = float(input("Enter a num1: "))  # 23.45
# num2 = float(input("Enter a num2: "))  # 34.567
# print(f"Addition of {num1} and {num2} is: ",num1 + num2)  # Addition of 23.45 and 34.567 is:  23.4534.567
# print(num1,type(num1), num2, type(num2))  #  before putting float <class 'str'> --- <class 'float'> after putting float

# round()
# num1 = float(input("Enter a num1: "))  # 234.56
# num2 = float(input("Enter a num2: "))  # 234.567
# print(f"Addition of {num1} and {num2} is: ",round(num1 + num2, 2))  #  469.13

print(round(123.435674, 3))   #  123.436
print('{:.3f}'. format(123.435674))  # 123.436


