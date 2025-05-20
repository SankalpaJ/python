'''encapsulation: binding private data..
    Python doesn't support encapsulation but it can be used by help of "getter()" & "setter()"..
    __var_name = private
    _var_name = protected

 '''
class Person:
    def __init__(self, name, age):
        self.name = name       # public var
        self.__age = age        # private var

    def get_age(self):        # to access use getter()
        return self.__age
    
    def set_age(self, newage): # to modfy use setter()
        self.__age = newage
p1 = Person("Alice", 33)
print(p1.name)
# print(p1.__age)   # error
print(p1.get_age())  # 33
p1.set_age(56)
print(p1.get_age())   # 56
'''
Alice
33
56
'''