class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
hold=None
class link:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def reverse(self):
        current=self.head
        p=None
        while(current!=None):
            t=current.next
            current.next=p
            current.prev=t
            p=current
            current=t
        self.head=p
    def print(self):
        current=self.head
        while(current!=None):
            print(current.data)
            current=current.next
i=Node(5)
lk=link()
lk.insert(i)
i=Node(7)

lk.insert(i)
i=Node(6)
lk.insert(i)
lk.print()
print("\n")

lk.reverse()
lk.print()
