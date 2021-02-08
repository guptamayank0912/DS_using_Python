
c=5
while c!=0:
    print(c)
    c-=1;


# while true:
#     response= input()
#     if(int(response) % 7==0):
#         break;

print("first\nsecond")


import math

# def Main():
#     num = float(input("Enter a number: "))
#     # fabs is used to get the absolute value of a decimal
#     print (num)
#     num = math.fabs(num) 
#     print(num)
# if __name__=="__main__":
#     Main()

a=["apple", "orange", "mayank"]
a[1]=7
print(a)
a.append("vsdfghsdghf")
print(a)

#dictionary
d={'alice': '9450046247', 'bob': '165465464', 'charles': 'sdfsdfs' }
print(d)

#for loop over a dictionary
nameMobile={'alice': '9450046247', 'bob': '165465464', 'charles': 'sdfsdfs' }
for namemob in nameMobile:
    print(namemob, nameMobile[namemob])    


#functions and its call
def square(x):
    return x*x
print(square(2631321313))

#empty return in the functon 
def oddoreven(x):
    if(x&1==1):
        print("odd")
        return
    else:
         print("even") 

oddoreven(31) #print the actual function call that is odd or even

print(oddoreven(31)) # print the return value function called first and printed odd then printed the return value
print(oddoreven(22))

#import other files and use their functions based on import

import words  #another file already present in the same folder
#words.fetch_word()

import words # second time nothing will get printed because file is already imported
