def Binarysearch(x):
    beg=0; end=len(l)-1

    while(beg<=end):
        mid= (beg+end)//2
        if(l[mid] == x):
            return mid
        elif(x<l[mid]):
            end=mid-1
        else:
            beg= mid+1
    return -1
    

l = [int (i) for i in input ("Enter value").split()]

x= int(input("Enter the element to search: "))

pos=Binarysearch(x)
if(pos>-1):
    print("Element found at: ",pos)
else:
    print("Element not found")