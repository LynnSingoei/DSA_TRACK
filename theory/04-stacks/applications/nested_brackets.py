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
