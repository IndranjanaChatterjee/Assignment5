class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
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
    def print(self):
        nodes=self.head
        while(nodes!=None):
            print(nodes.data)
            nodes=nodes.next
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

        
