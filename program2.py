class Solution(object):
    def romanToInt(s: str) -> int:
    # Dictionary to map Roman numerals to integer values
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    n = len(s)
    
    # Traverse through each character in the string
    for i in range(n):
        # Get the value of the current Roman numeral
        current_value = roman_to_int[s[i]]
        
        # Check if it's not the last character and if the next character has a larger value
        if i + 1 < n and current_value < roman_to_int[s[i + 1]]:
            # If the current value is less than the next, it's a subtractive pair
            total -= current_value
        else:
            # Otherwise, just add the value to the total
            total += current_value
            
    return total




