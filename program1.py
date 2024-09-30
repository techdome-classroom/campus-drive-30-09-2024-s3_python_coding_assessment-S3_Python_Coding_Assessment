class Solution(object):
   def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Use two pointers to traverse the string from left to right
        left = 0
        right = len(s) - 1
        
        # While the two pointers have not crossed each other
        while left < right:
            # Check for valid pairs at both ends
            if (s[left] == '(' and s[right] == ')') or (s[left] == '{' and s[right] == '}') or (s[left] == '[' and s[right] == ']'):
                left += 1
                right -= 1
            else:
                return False

        return left >= right







    



  

