class Solution(object):
    def isValid(self, s):
        stack = []
        elements = {"(": ")", "[": "]",  "{": "}"}
        for char in s:
            if char in elements:
                stack.append(char)
            elif len(stack)>0 and char ==elements[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        
        """
        Using stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
