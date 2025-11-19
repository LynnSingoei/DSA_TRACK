'''---
 Infix to Postfix Conversion (Stack Application)

## Problem Statement
- **Infix notation:** Operators are **between operands** → `A + B * C`  
- **Postfix notation (Reverse Polish Notation):** Operators are **after operands** → `A B C * +`  

We want to **convert infix expressions to postfix** to make evaluation easier for computers.  

**Example:**
Infix: A + B * C
Postfix: A B C * +

## Why Convert Infix to Postfix?

1. **Humans prefer infix:** `A + B * C` is easy to read.  
2. **Computers prefer postfix:** Evaluating postfix doesn’t require parentheses or worrying about operator precedence.  
3. **Stacks make evaluation easy:**  
   - Push operands onto a stack.  
   - Pop when an operator appears and apply it to the top operands.  
   - Postfix ensures correct order automatically.

---

## Algorithm / Intuition

1. Initialize an **empty stack** for operators and an **output list** for the result.  

2. **Scan the expression from left to right**:  

   - **Operand (letters/numbers):** Append directly to the output.  
   - **Opening parenthesis `(`:** Push onto the stack.  
   - **Closing parenthesis `)`:** Pop from stack to output until `(` is found, then discard `(`.  
   - **Operator (`+`, `-`, `*`, `/`, `^`):**  
     - While the stack is not empty AND the top has higher or equal precedence AND top is not `(` → pop top to output.  
     - Push current operator onto the stack.

3. **After processing all characters:**  
   - Pop any remaining operators from the stack to the output.  

---

## Step-by-Step Example

Expression: `(A+B)*C-D/E`  

1. Initialize `stack = []`, `output = []`.  

2. Read `(` → push to stack → `stack = ['(']`  
3. Read `A` → operand → output → `output = ['A']`  
4. Read `+` → operator → push → `stack = ['(', '+']`  
5. Read `B` → operand → output → `output = ['A', 'B']`  
6. Read `)` → closing parenthesis → pop until `(` → output = `['A', 'B', '+']`, stack = []  
7. Read `*` → operator → stack empty → push → `stack = ['*']`  
8. Read `C` → operand → output → `output = ['A', 'B', '+', 'C']`  
9. Read `-` → operator → `*` has higher precedence → pop `*` → output = `['A', 'B', '+', 'C', '*']` → push `-` → `stack = ['-']`  
10. Read `D` → operand → output → `output = ['A', 'B', '+', 'C', '*', 'D']`  
11. Read `/` → operator → `/` has higher precedence than `-` → push → `stack = ['-', '/']`  
12. Read `E` → operand → output → `output = ['A', 'B', '+', 'C', '*', 'D', 'E']`  
13. End → pop remaining operators → output = `['A', 'B', '+', 'C', '*', 'D', 'E', '/', '-']`  

✅ Postfix: `A B + C * D E / -`

---'''
from collections import deque
def infix_to_postfix(exp):
    stack=deque()
    output=[]
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}


    for char in exp:
        if char.isalnum():
            output.append(char)
        elif char=="(":
            stack.append(char)
        elif char==")":
            while stack[-1] !="(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1]!="(" and precedence.get(stack[-1],0)>=precedence[char]:
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

            
expr = "A+B/C*D-E/(F+G)"
print(infix_to_postfix(expr))