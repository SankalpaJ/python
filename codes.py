# Factorial of num:--- (same as sum of num)
N = int(input())
fact = 1
for i in range(1, N + 1):
    fact = fact * i        # sum = sum + i
print(f"The factorial of {N} is {fact}")

# fibonacci sequence:---
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a)
    res = a + b
    a,b = b, res

# sum of digits
# 12345 % 10 = 5 (any num % of 10 is last digit z d o/p)..
# 12345 // 10 = 1234 (any num // of 10 will removes d last digit..)
# 1) identify d last digit & extract d last digit (digit = num % 10)
# 2) add it to the sum
# 3) remove d last digit (num // 10)

num = int(input())
sum = 0
while(num > 0):
    digit = num % 10
    sum += digit
    num //= 10
print(sum)

# reverse of num
# 1) identify d last digit & extract d last digit (digit = num % 10)
# 2) reverse num * by 10 & add it to the digit
# 3) remove d last digit (num // 10)
num = int(input())
rev = 0
while (num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)
