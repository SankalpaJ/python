# class InvaildAge(Exception):
#     pass
# def checkAge(age):
#     if age < 18:
#         raise InvaildAge("Age must be greater than 18")
# checkAge(12)           # Error
'''
raise InvaildAge("Age must be greater than 18")
InvaildAge: Age must be greater than 18
'''

class InvaildAge(Exception):
    pass
def checkAge(age):
    if age < 18:
        raise InvaildAge("Age must be greater than 18")
try:
    checkAge(12)
except InvaildAge as e:
    print("Exception Occurred details are : ", e)   
'''
Exception Occurred details are :  Age must be greater than 18
'''



