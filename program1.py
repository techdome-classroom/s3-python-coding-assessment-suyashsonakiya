class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        # Mapping of closing to opening brackets
        matching_pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Iterate over each character in the string
        for char in s:
            # If the character is an opening bracket, push it to the stack
            if char in matching_pairs.values():
                stack.append(char)
            # If it's a closing bracket, check if it matches the last opened bracket
            elif char in matching_pairs.keys():
                # If stack is empty or the top of the stack does not match the current character
                if stack == [] or matching_pairs[char] != stack.pop():
                    return False
        # If the stack is empty, all brackets were matched correctly
        return stack == []






    



  

