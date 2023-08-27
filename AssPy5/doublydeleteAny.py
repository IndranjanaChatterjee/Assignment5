class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class link:
    def __init__(self):
        self.head=None
    def insertBeg(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insertEnd(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            
            ptr=self.head
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=newnode
            newnode.prev=ptr
    def insertAny(self,newnode,val):
        if(self.head==None):
            self.head=newnode
        else:
            
            ptr=self.head
            while(ptr.next!= None and ptr.data!=val):
                ptr=ptr.next
            newnode.next=ptr.next
            newnode.prev=ptr
            ptr.next.prev=newnode
            ptr.next=newnode
            
            
    
    
    def deleteAny(self,ele):
        strt=self.head
        
        while(strt.next!=None and strt.data!=ele):
            strt=strt.next
        ptr=strt
        strt.prev.next=strt.next
        strt.next.prev=strt.prev
        del ptr
    def print(self):
        nodes=self.head
        while(nodes!=None):
            print(nodes.data)
            nodes=nodes.next
n=int(input("Enter the number of nodes:"))
l=link()
for i in range (n):
    ele=int(input("enter the element in the list:"))
    enter=Node(ele)
    choice=int(input("enter 1 to enter at the beginning and 2 to add the end and 3 to enter at any position:"))
    match (choice):
           case 1:
             l.insertBeg(enter)
           case 2:
             l.insertEnd(enter)
           case 3:
             bef=int(input("Enter the element after which to be added:"))
             l.insertAny(enter,bef)
           case _:
             print("enter properly")
l.print()

bef=int(input("Enter the element to be deleted:"))
l.deleteAny(bef)
           
print("\n")
l.print()

        
