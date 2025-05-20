s1 = 'Code with Me,' 
print(s1[0])   # 0th index value from s1 string
print(s1[1])
print(s1[2])
print(s1[3])
print(s1[4])
print(s1[12])

print('Length of s1 is:', len(s1))    # length starts from 1 & index starts from 0

s2 = 'Code with kodnest...!'
print(len(s2))  # 21
print(s2[20])   # to find last char -> 1st find len -> put that index val
print(s2[-1])   # short cut to find last char which count from  reverse direction...

# String Slicing: creating new sub-string from main string....

s3 = "Kodnest"
sub_str = s3[0:3]  # s3[start index : end index-1]
print(sub_str)   # Kod
print(s3)     # Kodnest

print(s3[2:5])  # dne
print(s3[1:6])  # odnes

s4 = 'code'
s4.upper()
print(s4)  

# not converting upper-case,[BCZZ strings are ""immutable""]
# if we try to modify d string, it will create new string obj..
# if we want  to print the new string obj reference variable z must be present..

s4 = 'code'
s5 = s4.upper()  # creating reference variable s5
print(s4)         # code 
print(s5)           # CODE - converted to upper....

# strip()
# s1 = '    Code    '
# print(s1.strip())    # Code (removed extra spaces)
 
# s2 = '---Code---'
# new_str = s2.strip('-')
# print(new_str)          # Code (removed extra spaces(-))

# s3 = '----Hello---'
# print(s3.strip('-'))    # Hello
# print(s3.lstrip('-'))   # Hello---
# print(s3.rstrip('-'))   # ----Hello

# find()
# s2 = 'Code with me..!'
# print(s2.find('with'))   # 5



