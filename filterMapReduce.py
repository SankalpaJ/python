'''
 eval() :-- converts user input to "Tuple()" & also it automticaly 
            cnverts String to int insted of writing 
        li = input().split() we can use this "eval()"..

'Hello World!'.split()  # ['Hello', 'World!']
'Hello,World!.split()   # ['Hello,World!]
'10 20 30 40'.split()   # ['10', '20', '30', '40']

eval() --> grp of ele = "tuple"
eval() --> indivdual ele = their respective data type
ex: li = eval('10')
    print(li, type(li))   # 10 <class int>
'''

# li = list(eval(input('enter comma seperated ele: ')))
# print('Original ele: ', li)
# even_li = []
# def even(li):
#     for i in li:
#         if i % 2 == 0:
#             even_li.append(i)
# even(li)
# print('Even list: ', even_li)
'''
enter comma seperated ele: 10,20,30,40
Original ele:  [10, 20, 30, 40]
Even list:  [10, 20, 30, 40]
'''
#-----------------------------------------------------------------------

''' filter():-- it accepts 2 parameters 
                    1) function
                    2) iterable obj
    filter() z removeing unwanted ele and retunring some ele...
''' 

li = list(eval(input("Enter a comma seprated ele: ")))
print("Original List: ", li)
def even(ele):
    if ele % 2 == 0:
        return ele
even_li = list(filter(even, li))
print("Even list: ", even_li)
'''
Enter comma seprated values: 10,11,12,13,14,15
Original List:  [10, 11, 12, 13, 14, 15]
Even list:  [10, 12, 14]
'''
#---------------------------------------------------------------------------------

'''
map():-- modifying & retruning each ele in list.
        accepts 2 parameters:
          1) function
          2) iterable obj
'''
li = [1,2,3,4,5]
def square(ele):
    return ele ** 2
def cube(ele):
    return ele ** 3
sq_list = list(map(square, li))
print("square list: ", sq_list)  # square list:  [1, 4, 9, 16, 25]
cube_list = list(map(cube, li))
print("Cube list: ", cube_list)  # Cube list:  [1, 8, 27, 64, 125]

#---------------------------------------------------------------------------------------------

'''
reduce():--- returning 1 value from list
'''
from functools import reduce
li = [1,2,3,4,5]
def sum(a, b):
    return a + b
sum_res = reduce(sum, li)
print("sum ele: ", sum_res)   # sum ele:  15






