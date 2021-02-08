dict = {1: "Mayank", 2:"Shiva"}

print(len(dict))

print(dict[1])

print(dict.keys())

print(dict.values())

dict.update({2:"Aamir"})

print(dict.values())

#adding an element
dict[2] ="Salman" #this will update and add as well


dict.update({4:"Ram"}) #this will update and add as well

print(dict)

dict.pop(4)
print(dict)

for i in dict:
	print(i)
	print(dict[i])

#copy from one to another
mydict= dict.copy()
print(mydict)