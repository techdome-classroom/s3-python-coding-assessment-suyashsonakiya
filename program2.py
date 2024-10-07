class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize the total value
        total = 0
        # Iterate over each character in the string
        for i in range(len(s)):
            # If the current Roman numeral is smaller than the next one, subtract it
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            # Otherwise, add it to the total
            else:
                total += roman_to_int[s[i]]

        return total


