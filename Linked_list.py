class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

class Linkedlist:
    def __init__(self):
        self.head= None

    def insert_beg(self,x):
        new  = Node(x)
        if self.head == None:
            self.head = new
            return
        
        new.next = self.head
        self.head= new

    def delete_beg(self):
        if self.head == None:
            print("List is empty")
        self.head = self.head.next

    def displayList(self):
        if self.head ==None:
            print("List is empty")
            return
        temp=self.head
        while temp !=None:
            print (temp.data, end=" ")
            temp= temp.next


li= Linkedlist()
li.insert_beg(20)
li.insert_beg(10)
li.insert_beg(30)
li.displayList()
print()
li.delete_beg()
li.displayList()