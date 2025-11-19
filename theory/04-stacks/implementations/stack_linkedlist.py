#implementation using a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.count=0
    def push(self,val):
        new_node=Node(val)
        new_node.next=self.top
        self.top=new_node
        self.count+=1
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
        return self.count
    def display(self):
        curr=self.top
        while curr:
            print(f"| {curr.data} |")
            curr=curr.next
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.peek())
stack.display()
print(stack.size())
print(stack.peek())
