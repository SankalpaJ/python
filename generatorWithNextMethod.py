def disp():
    print("Start")    # dataset 1
    yield 10
    print("Task 1")   # dataset 2
    yield 20
    print("Task 2")   # dataset 3
    yield 30
res = disp()
# print(res)      # <generator object disp at 0x000001768BD25F00>
# print(res.__next__())   # Start   10 
# print(res.__next__())
# print(res.__next__())

# using for-loop :-- in same sequence we want to ask to print..
for i in range(2): 
    print(res.__next__())
'''
Start
10
Task 1
20
'''
# for i in res:
#     try: 
#         print(res.__next__())
#     except:
#         print("There z no next value stop this iteration..")
'''
Start
Task 1
20
Task 2
There z no next value stop this iteration..
'''

# iterator-----------------------------
def disp():
    print("Start")
    yield 10
    print("Task 1..")
    yield 20
    print("Task 2")
    yield 30
res = disp()
for i in res:
    print(i)
'''
Start
10
Task 1..
20
Task 2
30
'''