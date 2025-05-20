# shows address ..
s1 = 'Code'
s2 = 'World'
print(s1, id(s1))   # Code 140705937032104
print(s2, id(s2))    # Word 140705937096864

# shows id of particular char
print(id(s1[0]))   # 140705937095232
print(id(s1[3]))

print("Address of 'o' in s1 is:", id(s1[1]))  # Address of 'o' in s1 is: 140705933165184 
print("Address of 'o' in s2:", id(s2[1]))       # Address of 'o' in s2: 140705933165184 

