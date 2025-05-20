# iterable obj:- any obj which grps multiple values. ex: range(0, 5)
# only which as index value we can iterable...

# to print Squre of each ele in list
li = [2, 3, 4]
for i in li:         # creating duplicate list of li
    print(i ** 2, end = "-")  # 4-9-16-

# to create list of squre of  each ele of li list.
l1 = [2, 3, 4, 5]
sq = []
for i in l1:
    sq.append(i**2)
print('Squre list is: ', sq)  # Squre list is:  [4, 9, 16]

# list comp:--
# syntax:--  [exp(return_var)  for control_var(i) in iterable_obj]
l1 = [2, 3, 4, 5]
print([i**2 for i in l1])   # [4, 9, 16, 25]

# adding +5 for each ele in list
l1 = [2,  3, 4]
print([i+5 for i in l1])   # [7, 8, 9]

# to print even num in list
# Syntax: [exp(return_var) for control_var(i) in iterable_obj condition]
li = [1, 2, 3, 4, 5, 6]
print([i for i in li if i % 2 == 0])   # [2, 4, 6]

'''
List comp:----
1) Syntax: [exp(return_var)  for control_var(i) in iterable_obj]
2) Syntax: [exp(return_var) for control_var(i) in iterable_obj condition]

'''
