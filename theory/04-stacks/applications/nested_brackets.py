from collections import deque
"""
Check if a string has valid nested brackets.


This function uses a stack to ensure that each opening bracket
has a corresponding closing bracket in the correct order.


Args:
s (str): A string containing brackets '()', '{}', '[]'.


Returns:
str: "Valid expression" if the brackets are correctly nested,
or an error message describing why it's invalid.


Examples:
>>> nested_brackets("{[()]}")
'Valid expression'


>>> nested_brackets("{[(])}")
'Invalid: brackets do not match'


>>> nested_brackets("((()))")
'Valid expression'


>>> nested_brackets("((())")
'Invalid: more opening brackets than closing'
## Algorithm

1. Initialize an empty stack.

2. Create a **mapping** from closing → opening brackets:
```python
bracket_map = {')':'(', '}':'{', ']':'['}

    Loop through each character in the string:

        If it’s an opening bracket, push onto the stack.

        If it’s a closing bracket:

            If the stack is empty → invalid (extra closing bracket)

            Pop the top of the stack → if it doesn’t match the correct opening → invalid

    After looping, check the stack:

        If the stack is not empty → invalid (extra opening brackets)

        Else → valid
"""
def nested_brackets(s):
    stack=deque()
    brackets_map={")":"(","]":"[","}":"{"}
    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        else:
            if not stack:
                return "Invalid more closing brackets than opening"
            elif not stack.pop()==brackets_map[char]:
                return "Invalid the brackets do not match"
            
    if stack:
        return "Invalid more opening brackets than closing"
    return "Valid"

print(nested_brackets("{[()]}"))       
print(nested_brackets("{[(])}"))      
print(nested_brackets("((())"))
