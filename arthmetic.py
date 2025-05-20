num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
choice = input("Enter Choice : Add-1, Sub-2, Mul-3, Div-4:, SquareOfNum-5, floorDiv-6, mod-7: ")
if choice == '1':
    print("Addition is:", num1 + num2)
elif choice == '2':
    print("Subtraction is:", num1 - num2)
elif choice == '3':
    print("Multiply is:", num1 * num2)
elif choice == '4':
    print("Division is:", num1 / num2)
elif choice == '5':
    print("SquareOfNum is: ",num1 ** 2)
    print("SquareOfNum is: ",num2 ** 2)
elif choice == '6':
    print("Floor division is: ", num1 // num2)  # it will rounds up the result to nearest num....
elif choice == '7':
    print("Modulos is: ", num1 % num2)
else:
    print("Invaild Choice...!!")
