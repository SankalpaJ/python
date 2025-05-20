# iterator will always generates values
li = [10, 20, 30] # iterable
iterator = iter(li)     
print(iterator.__next__()) # 10
print(iterator.__next__()) # 20
print(iterator.__next__()) # 30
print(iterator.__next__()) # StopIteration

# iterClass:------
# __iter__()  it returns address of that obj(ex Counter)
class Counter:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            raise StopIteration
c1 = Counter(5)
print(c1.__iter__())
print(c1.__next__())  # 1
print(c1.__next__())  # 2

# https://github.com/Priya9096/Python-Codes-2025- [ with hacker Rank]
# https://github.com/Priya9096/Python-Project-CRUD

