class Solution(object):
   def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:

            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
          
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        # If the stack is empty, all the parentheses are valid
        return not stack







    



  

