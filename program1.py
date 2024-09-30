class Solution(object):
 def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracketsMap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
      
        if len(s) == 1 or s[0] in bracketsMap:
            return False
        # Have astack to hold the opening brackets
        openingBrackets = []
        # Iterating the string
        for index in range(len(s)):
            # Current character
            currentBracket = s[index]
            if currentBracket not in bracketsMap: # It's an opening bracket
                openingBrackets.append(currentBracket)
                # Moving on to the next character
                continue
            else: # We have a closing bracket
                # Matching bracket
                matchingBracket = bracketsMap[currentBracket]
                # Grabbing top bracket from stack
                if not len(openingBrackets):
                    return False
                candidateBracket = openingBrackets.pop()
                # Comparing the two
                if matchingBracket != candidateBracket:
                    return False
                else: # We have a valid string so far
                    continue
        # Takes care of 2 things at once. If we've iterated the entire string and have a valid string we should return True. But we also make sure that the stack is empty in the case of all '((((('
        return not len(openingBrackets)






    



  

