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
#implementation using dynamic arrays(lists in python)
class ArrayStack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def display(self):
        for item in reversed(self.stack):
            print(f"| {item} |")
#implementation using collections.deque
from collections import deque
class DequeStack:
    def __init__(self):
        self.stack=deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def display(self):
        for item in reversed(self.stack):
            print(f"| {item} |")
    

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.peek())
stack.display()
print(stack.size())
print(stack.peek())
print(stack)
