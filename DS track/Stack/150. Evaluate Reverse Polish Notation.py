'''
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''

'''
one thing to notice in this question is that, if we get - or / in the token, it's the second char -/ first char
+ or * doesn't matter
with that saying, we can use a stack to store the tokens seen, if it's an espression, we do the calculation, otherwise we append it in stack
'''

'''
create a stack
for token in tokens
if token == / or - or + or *:
  a = stack.pop() -> first char
  b = stack.pop() -> second char
  res = the calculation result
  stack.append the calculation result
else:
  meaning we met with numbers, stack.append
return stack.pop
'''

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                res = b+a
                stack.append(res)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                res = b-a
                stack.append(res)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                res = b*a
                stack.append(res)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(b/float(a))
                stack.append(res)
            else:
                stack.append(int(t))
                
        return stack.pop()
                
        
        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        
