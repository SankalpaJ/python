# Symmetric :-- Unique ele will be returened....
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 6, 7}
new_set = s1.symmetric_difference(s2)
print(new_set)                     # {4, 5, 6, 7}

# converting list to set...
print(set([1,2,3,4]))          # {1, 2, 3, 4}


# subset
st1 = {10, 20, 30}
st2 = {10, 20, 30, 40, 50}
print(st1.issubset(st2))     # True

# Symmetric d/f b/w 2 sets:---
s1 = set(map(int,input("Enter set1: ").split()))
s2 = set(map(int,input("Enter set2: ").split()))
s3 = s1.symmetric_difference(s2)
list = sorted(s3)          # "sorted" func used to retrive result in asending order 
print("Symmteric eles: ",list)

'''
Enter set1: 10 20 30 40
Enter set2: 20 35 30 35
Symmteric eles:  [10, 35, 40]
'''

