""" Data Structure(DS) :- organizing data of related data in database
   which is easy to manuplate, organize, retrive & etc..
   [] --            List
   () --            tuple
   {} --            set
   {key : value} -- dict --> these are Advance Data Types.....
"""
# List
# li1 = [10, 20, 30, 40]
# print(li1, type(li1))   # [10, 20, 30, 40] <class 'list'>

li1 = [10, 20, 30, 10, 'Code', True, 66.7]
print(li1, type(li1))          # [10, 20, 30, 10, 'Code', True, 66.7] <class 'list'>

print(li1[0])   # 10
print(li1[1])   # 20
print(li1[2])   # 30
print(li1[4])   # Code

li1[3] = 'MyCode'
print("After Update: ", li1)  # After Update:  [10, 20, 30, 'MyCode', 'Code', True, 66.7] 

""" 
1. List is homogeneous and heterogenous type of data.
2. List z an Ordered Collection of data. List maintains order insertion in the o/p
    thats why we call it is Ordered Collection of data.
3. In this we can store duplicate values...
4. Using their index values we can access it..
5. Lists are Mutable...

"""