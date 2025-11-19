#implementation using a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,val):
        new_node=Node(val)
        new_node.next=self.top
        self.top=new_node
        self.size+=1
    def pop(self):
        if self.top:
            popped=self.top.data
            self.top=self.top.next
            self.count-=1
            return popped
    def peek(self):
        return self.top.data if self.top else None
    def is_empty(self):
        return self.top is None
    def size(self):
        return self.size
    def display(self):
        curr=self.top
        while curr:
            print(f"| {curr.data} |")
            curr=curr.next