class Solution(object):
def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    
    # HashMap to keep mappings of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Traverse through each character in the input string
    for char in s:
        # If the character is a closing bracket
        if char in mapping:
            # Pop the topmost element from the stack if it is not empty, otherwise assign a dummy value '#'
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element is the matching opening bracket
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push onto the stack
            stack.append(char)
    
    # In the end, the stack should be empty if the input string is valid
    return not stack








    



  

