'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
The key to this question is to understand what does "valid" means, not only (){} are valid, but also {()}. But {(}) is not valid
'''

'''
we will create a dictionary, with all close bracket as key, open bracket as value
create a stack to store chars from the input string
for each close bracket we got, we pop the stack, if the value is equal to the value in the dic, we continue, otherwise return False
out of the loop, we return if the stack length is equal to 0
'''

class Solution(object):
    def isValid(self, s):
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for c in s:
            if c in brackets and stack:
                top = stack.pop()
                if top!= brackets[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack
            
        """
        Time complexity :O(n)
        Space Complexity : O(n)
        """
        
