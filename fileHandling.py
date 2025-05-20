f1 = open("fileDemo.txt")
data = f1.read()
print(data)
'''
Hello from text decumnet       
Data coming from fileDemo.txt..
'''

# "with" keyword :- opening a file
with open('fileDemo2.txt','r') as f1:
    data = f1.read()
    print(data)
    
#----------------------------------------------------------------
# write mode

# f2 = open('fileDemo2.txt', 'w')
# f2.write('Added Data in demo2')
# f2.close()    # Data coming from fileDemo.txt..
#-------------------------------------------------------------------------

# append mode
f3 = open('fileDemo2.txt', 'a')
f3.write('\nAdded new data')
f3.close()

#-----------------------------------------------------------------
'''
'r':-- Read opens d file for reading 
'w':-- writes
'a':-- append

'''