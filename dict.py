# [10,20,30] -- List--> mutable
# (10,20,30) -- tuple --> imutable
# {10,20,30} -- set --> Mutable

'''
1. Both hemo & heterogenous type of data stored..
2. Orderd Collection of data
3. Doesn't contain duplicate values..
'''
# Dict--> {key-value} pairs
# d1 = {
#     'name' : 'Sankalpa J',
#     'age' : 20,
#     'phone' : 234,
# }
# print(d1, type(d1))  # {'name': 'Sankalpa J', 'age': 20, 'phone' : 234} <class 'dict'>

d1 = {
    'name' : 'Sankalpa J',
    'age' : 20,
    'phone' : 234,
    'Math' : 74,
    'Science' : 60,
    'name' : 'Thanu',
    'ID' : 101
}
print(d1, type(d1)) 
# {'name': 'Thanu', 'age': 20, 'phone': 234, 'Math': 74, 'Science': 60, 'ID': 101} <class 'dict'>

# Accessing  dict values..
print(d1['name']) # Thanu
print(d1['Math']) # 74

# Acessing keys using for-loop
for i in d1.keys():
    print(i, end = "-")
print()                  # name-age-phone-Math-Science-ID-

# Acessing values using for-loop
for i in d1.values():
    print(i, end = "-")  # Thanu-20-234-74-60-101-
print()

# Acessing both key & values using for-loop
for i in d1.items():
    print(i)

'''
('name', 'Thanu')
('age', 20)
('phone', 234)
('Math', 74)
('Science', 60)
('ID', 101)             ----- in form of tuple we get o/p
'''
# kopApp -- Contact details prlm...
contact = {}
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    name, phone = user_input.split(",")
    contact[name.strip()] = phone.strip()
for name, phone in contact.items():
    print(f"{name}: {phone}")