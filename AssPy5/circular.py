class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class link:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if(self.head==None):
            newnode.next=newnode
            self.head=newnode
        else:
            ptr=self.head
            while(ptr.next!=self.head):
                ptr=ptr.next

            ptr.next=newnode
            newnode.next=self.head
            self.head=newnode
            
    def print(self):
        nodes=self.head
        while(nodes.next!=self.head):
            print(nodes," ",nodes.data," ",nodes.next)
            nodes=nodes.next
        print(nodes," ",nodes.data," ",nodes.next)
print("kk")
first=Node(4)
l=link()
l.insert(first)

second=Node(5)
l.insert(second)
third=Node(6)
l.insert(third)
th=Node(7)
l.insert(th)
thi=Node(8)
l.insert(thi)
l.print()

        
