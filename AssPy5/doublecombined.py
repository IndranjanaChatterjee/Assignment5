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
            
            
    def deleteBeg(self):
        strt=self.head
        self.head=strt.next
        self.head.prev=None
        del strt
    def deleteEnd(self):
        strt=self.head
        
        while(strt.next.next!=None):
            strt=strt.next
        ptr=strt.next
        strt.next=None
        del ptr
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
print("kk")
first=Node(4)
l=link()
l.insertBeg(first)

second=Node(5)
l.insertBeg(second)
third=Node(6)
l.insertEnd(third)
th=Node(7)
l.insertBeg(th)
thi=Node(8)
l.insertEnd(thi)

thi=Node(9)
l.insertAny(thi,5)
l.print()
print("\n")
l.deleteAny(6)
l.print()
""" l.deleteEnd()
print("\n")
l.print()
l.deleteEnd()
print("\n")
l.print()
l.deleteBeg()
print("\n")
l.print() """

        
