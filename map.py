# map -> accepts 2 parametrs (func, iterable obj)...
# wt it return as result we can convert it into list, tuple & etc....
li = [1, 2, 3, 4]
def square(ele):
    return ele * ele
res = map(square, li)   # 'res' z holding address of iterable obj(li)
print(res)   # <map object at 0x000001EC60EDAD40>
# here map will return 1 obj and that obj we are converting as list...
print(list(res))  # [1, 4, 9, 16]


# converting string data in list to int...(insted of using nrml for-loop we use 'map' func)...
li2 = ['10', '20', '30', '40']
print(li2)                     # ['10', '20', '30', '40']
newLi = list(map(int, li2))
print(newLi)                    # [10, 20, 30, 40]

li3 = [1, 2, 3, 0]
print(list(map(float, li3)))    # [1.0, 2.0, 3.0, 0.0]

print(list(map(bool,li3)))      # [True, True, True, False]



