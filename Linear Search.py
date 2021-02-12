l = [int (i) for i in input ("Enter value").split()]

x= int(input("Enter the element to search: "))

for i in l:
    if i==x:
        print('Element found')
        break
else:
    print("Element not found")