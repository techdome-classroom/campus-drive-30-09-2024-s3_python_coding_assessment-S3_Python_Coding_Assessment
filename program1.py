class Solution(object):
   def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket does not match the top element
                if mapping[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all the parentheses are valid
        return not stack







    



  

