# decorators are nothing but function & it always accept parameter as func...

def decor(function):
    def inner(name):
        if name == 'Aysuh':
            print(name, 'likes Biryani...')
        else:
            return function(name)
    return inner
@decor
def process(name):
    print(name, 'likes pulao')
process('Ankit')
process('Akash')
process('Aysuh')
process('Punith')
'''
Ankit likes pulao
Akash likes pulao
Aysuh likes Biryani...
Punith likes pulao
'''


def smartdiv(function):
    def inner(a, b):
        if b == 0:
            print('Not Possible..')
        else:
            return function(a, b)
    return inner
@smartdiv
def div(a, b):
    print(a / b)
div(10, 2)    # 5.0
div(20, 5)    # 4.0
div(10, 0)    # Not Possible..
