def process(a,b):
    print(a/b)
   #print(a/c)  # nameError
try:
    process(10, 0)
except ZeroDivisionError:
    print("ZeroDivision Erroroccured & Handled")
except NameError:
    print("NameError Erroroccured & Handled")
except TypeError:
    print("typeError Erroroccured & Handled")
except:
    print("some other Erroroccured & Handled")
print("Next Tasks")