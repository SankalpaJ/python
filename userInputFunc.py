# WAC to print addition of 2 num by taking user input...
# 1st way:--
def add():
    a = int(input('Enter value for a: '))    # Enter value for a: 12
    b = int(input('Enter value for b: '))    # Enter value for b: 32
    print("Sum is: ", a+b)                   # Sum is:  44
add()

# 2nd way:--
def add1(a,b):
    print("Sum is: ", a+b)
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
add1(a,b)