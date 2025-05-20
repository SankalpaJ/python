# s1 = "This is a test. This test is simple."
# s1 = s1.replace('.'," ")
# print(s1)
# print(s1.count('is')) # -- it gives substring is as 4 times

# s1 = "This is a test. This test is simple." .replace('.' , " ") .split()
# di = {}
# for i in s1:
#     if i in di:
#         di[i] = di[i] + 1
#     else:
#         di[i] = 1
# print(di)        # {'This': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}

s1 = "This is a test. This test is simple." .replace('.' , " ") .split()
di = {}
for i in s1:
    if i in di:
        di[i] = di[i] + 1
    else:
        di[i] = 1
for key in di.keys():
    print(f'{key}: {di[key]}')
'''
This: 2
is: 2
a: 1
test: 2
simple: 1
'''
# https://github.com/Priya9096/Python-Codes-2025- [ with hacker Rank]
# https://github.com/Priya9096/Python-Project-CRUD