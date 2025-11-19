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