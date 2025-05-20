# Method Chaining z nothing but calling 1 method from another method
# class GrandParent:
#     def cook(self):
#         print('GrandParent cooks Biryani..')
# class Parent(GrandParent):
#     def cook(self):
#         print('Parent cooks Pulao...')
# class Child(Parent):
#     def cook(self):
#         print('Child cooks Maggie......')
#         super().cook()
# c = Child()
# c.cook()
'''
Child cooks Maggie......
Parent cooks Pulao...
'''

class GrandParent:
    def cook(self):
        print('GrandParent cooks Biryani..')
class Parent(GrandParent):
    def cook(self):
        print('Parent cooks Pulao...')
class Child(Parent):
    def cook(self):
        print('Child cooks Maggie......')
        super().cook()
        super(Parent,self).cook()  # methodChaining
c = Child()
c.cook()
'''
Child cooks Maggie......
Parent cooks Pulao...
GrandParent cooks Biryani..
'''

