# converting String to List using split()............
s1 = 'A B C D'
li = s1.split()
print(li)           # ['A', 'B', 'C', 'D']

# converting List to String using join().......
new_str = ''.join(li)    
print(new_str)      # ABCD
new_str = '-'.join(li)
print(new_str)      # A-B-C-D

s2 = 'Hello World'
print(s2.split())   # ['Hello','World']

li = ['Hello','World']
print("".join(li))  # 'Hello World'