'''
 Reverse a String Using a Stack

## Problem Statement
Given a string, reverse it using a stack.

**Example:**
Input: "HELLO"
Output: "OLLEH"

Why Use a Stack?
- A **stack** follows **Last In, First Out (LIFO)**.  
- If we push each character of a string onto a stack:
  - The **last character ends up on top**.  
  - Popping characters one by one gives them in **reverse order**.  

Think of it like **stacking books**:  
- Place letters on top of each other → `H` at bottom, `O` at top.  
- Take them off → `O` comes out first, `H` last → reversed string.

---

## Algorithm
1. Create an empty stack.  
2. Push each character of the string onto the stack.  
3. Pop characters from the stack one by one and append them to a new string.  
4. Return the new string as the reversed string.

---
'''
def reverse_a_string(s):
    stack=[]
    reverse=""
    for char in s:
        stack.append(char)
    while stack:
        reverse+=stack.pop()
    return reverse
original = "HELLO"
reversed_str = reverse_a_string(original)
print(reversed_str)