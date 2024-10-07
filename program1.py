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

       
        for char in s:
           
            if char in matching_pairs.values():
                stack.append(char)
            
            elif char in matching_pairs.keys():
                # If stack is empty or the top of the stack does not match the current character
                if stack == [] or matching_pairs[char] != stack.pop():
                    return False
        # If the stack is empty, all brackets were matched correctly
        return stack == []






    



  

