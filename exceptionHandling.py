'''
1) try {}    :-- when exptn occurs in try block then control will reach respective "expect block"
                  when there z "no expection" in logic which z present in try block then respective "else block" will be executed..
2) expect{} :--
3) else {}  :--
4) finally {} :-- it always be executed..

Exptn handling occurs whenever in code it struck with abrapt(sudden) terminate it won't execte code
           it moves to PVM to avoid that and run all instrctions we use these try, execpt & soo on....
they are unexpected events that can stop ur prgm.
2 types:-- 1) complie time Error:-- phase while coverting from "source code" to "byte code"
           2) Run-time Error:--   from "byte code" to "PVM" (Syntax, logical error)  ex: ZeroDivisonError 10/0, NameError, TypeError
                 logical error z also "Human error"

'''

# Exception:--
# def add(a,b):
#     print("Start")
#     print(a/b)
#     print("End")
# add(10, 0)             # ZeroDivisionError
# print("Other Tasks")

# try & expect:-------------
def add(a,b):
    print("Start..")
    print(a/b)
try:
    add(10, 0)
except:
    print("Exception occured & handled..")
else: 
    print("There is no Expection")
finally:
    print("End")
print("Other Tasks..")

'''
add(10, 2)
Start..
5.0
There is no Expection
End
Other Tasks..
----------------------------------
add(10, 0)
Start..
Exception occured & handled..
End
Other Tasks..
'''