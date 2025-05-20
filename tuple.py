t1 = (10, 20, 20, 'Code', True)
print(t1)        # (10, 20, 20, 'Code', True)
print(t1, type(t1))
print(t1[0])  # 10
print(t1[4])  # True
t1[0] = 300
print(t1) # Error -> 'tuple' object does not support item assignment 

# Unpacking Tuple:---
t2 = (100, 200, 300, 50)
e1, e2, e3, e4 = t2
print(f"e1: {e1}, e2: {e2}, e3: {e3}, e4: {e4}")  # e1: 100, e2: 200, e3: 300, e4: 50

'''
(100, 200, 300, 400) =>  packed tuple
100, 200, 300, 400   => unpacked tuple 
'''

# combining
tup1 = (10, 20)
tup2 = (30, 40)
# print(tup1 + tup2) # (10, 20, 30, 40)
newtup = tup1 + tup2
print(newtup)    # (10, 20, 30, 40)
print(len(newtup))  # 4

# to find index of ele:--- use "index()" and also use "in" operator....
num = tuple(map(int, input("Enter numbers: ").split()))
ele = int(input("Enter num to find: "))
if num in ele:
    index = num.index(ele)
    print(f"The index of {ele}: {index}")
else:
    print("Element not found in tuple.")

'''
Enter number: 10 20 30 40 50
Enter num to find: 30
The index of 30: 2
'''
# exact elements at even indices using tuple scling use "[start:end:inc/dec]"
num = tuple(map(int, input("Enter the  num: ").split()))
even = num[::2]
print("Elemets of even indices:", even)
'''
Enter the num: 10 20 30 40 50
Elemets of even indices: (10, 30, 50)

'''
# ----------------------------------------------------------
'''
1. It stores both hemo & hetrogeneous data.
2. Ordered Collection of data.
3. Stores duplicate values.
4. It is immutable. We can delete the Tuple.....

'''