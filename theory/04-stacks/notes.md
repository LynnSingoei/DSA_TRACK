## 📚 Stack Notes (Markdown Version)
## 🧱 What is a Stack?

A stack is a linear data structure that follows the LIFO (Last In, First Out) principle. Think of a pile of plates: the last one you put on top is the first one you take off.

## 🧠 Core Operations

| Operation | Meaning |
|-----------|---------|
| push(x)   | Add an element to the top |
| pop()     | Remove and return the top element |
| peek()    | Return the top element without removing it |
| is_empty()| Check if stack is empty |
| size()    | Return number of elements |

## Time & Space Complexity

| Operation   | Time Complexity | Space Complexity |
|------------|----------------|-----------------|
| push       | O(1)           | O(n)            |
| pop        | O(1)           | O(n)            |
| peek       | O(1)           | O(n)            |
| is_empty   | O(1)           | O(1)            |
| size       | O(1)           | O(1)            |

## Methods of Implementations

- 🏗️ Implementation 1: Linked List Stack
- 🧰 Implementation 2: Dynamic Array (Python list)
- ⚙️ Implementation 3: deque Stack (from collections)

## Applications of Stacks

Here’s where stacks stop being theory and actually become useful:

## 1. Undo/Redo Functionality

Used in editors like VS Code, Word, Google Docs.
Every action you perform is pushed onto a stack.
Undo = pop.
Redo = pop from another stack.

## 2. Backtracking Algorithms

Such as:

DFS (Depth First Search)

Solving mazes

Navigating recursion manually

When you need to "go back" to a previous step → stack.

## 3. Browser Back/Forward Navigation

Every site you visit goes into a stack.
Back button = pop.
Forward button = push into a second stack.

## 4. Expression Evaluation

Like:

Postfix expression evaluation

Infix → postfix conversion

Checking balanced parentheses "(){}[]"

These are classic interview questions.

## 5. Function Call Stack

Every time a function is called, Python pushes it onto the call stack.
When it returns, it is popped.
This is why recursion relies so heavily on stacks.

## 6. Reversing Data

Reversing strings

Reversing linked lists (sometimes)

Reversing order of operations

If it needs flipping, stacks do it.

## 7. Memory & System Operations

Interrupt handling

Backtracking in compilers

Managing symbol tables

Pretty much every OS uses stacks somewhere.

## When to Use a Stack?

Undo/redo operations

Browser back/forward history

Expression evaluation (postfix/prefix)

DFS in algorithms

## Common Interview Questions Using Stacks

Valid Parentheses

Min Stack

Evaluate Reverse Polish Notation

Simplify Path

Next Greater Element

Daily Temperatures

Decode String

## Patterns to Recognize

When the problem talks about “undo,” “reverse,” “track previous state,” or “backtrack,” think stack.

If the problem looks like matching or nesting → stack.

If recursion can solve it but you want iterative → stack
