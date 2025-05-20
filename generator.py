# we can return multiple values from func using return statemnt
def process():
    return 30
res = process()
print(res)         # 30

# can we return multiple values from a func using yield keyword? "YES"
def disp():    # generator func
    yield 10
    yield 20
    yield 30
res = disp()    # calling of generator func
print(res)  # Generator iterator Obj <generator object disp at 0x000001B9E9D45BC0>
print(res.__next__())  # 10
print(res.__next__())   # 20
print(res.__next__())    # 30
print(res.__next__())   # StopIteration -- Error

'''
1) a func which as "yield keyword" in  it z known as "generator"
2) generator func used when we have "large datasets". to fetch some data again & again which ever & whenever we want,
    but when we use nrml func it return all values present in it, in 1 shot..
3) they generate values "on fly"  using "(obj_name.__next__())"
4) we can save memory which condition z active that value only stored in memory other values are removed..
        at a time only 1 dataset z present in it..
'''

