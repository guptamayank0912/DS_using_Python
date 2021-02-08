ls= [10,20,30,40,50]

ls.append(500)
print(ls[::-2])

#want to add new element at index 4
ls.insert(3, 12)
print ("print after insert:",ls)

#delete operation
ls.pop()
print("print after pop:",ls)

ls.sort()
print ("sorted list:",ls)

print(ls.index(20))

list=[3,8,5,20,5]
print(list.index(5))

