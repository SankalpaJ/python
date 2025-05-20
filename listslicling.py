# list[start: end-1: increment/decrement]
li = [10, 20, 30, 40, 50]
print(li[::])      # [10, 20, 30, 40, 50]
print(li[::2])      # [10, 30, 50]     --> not consider 'end -1'[bcz we not given end val]
print(li[1::])      # [20, 30, 40, 50]
print(li[:3:])      # [10, 20, 30]
print(li[1:4:2])    # [20, 40]  
print(li[: : -1])   # [50, 40, 30, 20, 10]

# Kod App prlm-- Extract a sublist using list slicing

user_input = input().split()
li = list(map(int,user_input))
start = int(input())
end = int(input())
print("Exttracted sublist: ", li[start: end: ])

'''
10 20 30 40 50
1
5
Exttracted sublist:  [20, 30, 40, 50]
'''

# squre of  each ele in list
li = list(map(int, input().split()))
sq = [i ** 2 for i in li]
print("List of sqrs: ", sq)
'''
1 2 3 4 5
List of sqrs:  [1, 4, 9, 16, 25]
'''

# Occurencnce of ele [we can't directly use Union or Insertion bcz these are 'set' oprns]
li = list(map(int, input().split()))
for i in set(li):          # here if we don't use set it gives duplicte 'printf' data... u can see by remeoving 'set'..
    print(f"{i} occurs {li.count(i)} time(s)")
'''
1 2 3 4 1 2 2 1 3
1 occurs 3 time(s)
2 occurs 3 time(s)
3 occurs 2 time(s)
4 occurs 1 time(s)
'''
# using tuple find odd or even
tup = tuple(map(int, input().split()))
even = []
odd = []
for i in tup:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even: ", len(even))
print("Odd: ", len(odd))

'''
1 2 4 3 5 6 7
Even:  3
Odd:  4
'''
