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
        openingBrackets = []
        # Iterating the string
        for index in range(len(s)):
            # Current character
            currentBracket = s[index]
            if currentBracket not in bracketsMap: 
                openingBrackets.append(currentBracket)
                # Moving on to the next character
                continue
            else: 
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
        return not len(openingBrackets)






    



  

