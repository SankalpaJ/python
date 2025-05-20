# s1 = {10, 20, 20, True, 'Code'}
# print(s1, type(s1))   # {True, 10, 'Code', 20} <class 'set'>

# s1.add(500)
# print(s1)  # {True, 10, 'Code', 20, 500}

# s1.remove(500)
# print(s1)    # {True, 'Code', 10, 20}

# s1.remove(2000)
# print(s1)      # KeyError: 2000 ---> bcz s1 not as 2000 ele...


# Union :- All d ele from both d set...
# s1 = {1, 2, 3, 5}
# s2 = {3, 4, 5}
# new_set = s1.union(s2)
# print(new_set)    # {1, 2, 3, 4, 5}

# intersection:- to find common ele in 2 sets
# s1 = {1, 2, 3, 5}
# s2 = {3, 4, 5}
# s3 = s1.intersection(s2) # {1, 2, 3, 4, 5}
# print(s3)                #  {3, 5}

# to find common ele in 2 sets
# s1 = set(map(int, input("Enter set1:").split()))
# s2 = set(map(int, input("Enter set2:").split()))
# s3 = s1.intersection(s2)
# list = sorted(s3)    # convets list to sets and results asending order...
# print("Common ele:",list)
'''
Enter set1:10 20 30  40 50
Enter set2:20 10 50 60 35
Common ele: [10, 20, 50]
'''

# find difference b/w 2 sets
# s1 = set(map(int, input("Enter set1: ").split()))
# s2 = set(map(int, input("Enter set2: ").split()))
# s3 = s1.difference(s2)
# print("Ele in set 1 but not in set 2: ", s3)
'''
Enter set1: 1 2 3 4 5 6
Enter set2: 2 3 1 4 6 7
Ele in set 1 but not in set 2:  {5}
'''

# checking 2  sets are disjoint or not
s1 = set(map(int, input("Enter set1: ").split()))
s2 = set(map(int, input("Enter set2: ").split()))
if s1.isdisjoint(s2):
    print("The sets are disjoint.")
else:
    print("The sets are disjoint.")
'''
Enter set1: 1 2 3 4
Enter set2: 6 7 8 9
The sets are disjoint.
'''
# --------------------------------------------------
'''
1. Stores both homo & heterogenous data.
2. Set z a UnOrdered Collection of data (bcz it genertates
    the o/p in random order.)
3. It does not maintain order of insertion in output.
4. Set is Mutable. 
5. It doesn't contain duplicate values.
6. It not support indexing of an element [bcz Order of o/p doesn't matching with Order of insertion]..
'''
