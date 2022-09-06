'''
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

'''
 For this question, it's important to understand what "valid" means. 
 We simply have 3 rules:
 1. if the number of open paran > n, we can't add any open
 2. if the number of close >= open, we can't add any close
 3. if number of close = open = n, we stop for this paranthese.
 This is just for one parathese, we need to generate all possible ones
 So we should use recursion, use two if loop as the two splits in a tree
 '''

'''
create a stack to store the parathesis, create a stack to store the results
in the recursion
if number of close = open = n -> add all in stack to res as string and return
if the number of open paran < n, we add one ( into stack, run the recursion-> continue with this split, and stack pop to clean what we have here because stack is global variable
if number of close <open, we add one ) , run the recursion, stack pop as well
out of the recursion,
run the recusion with starter (0,0) -> number of close and open both 0
and return res
'''

class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        
        def getParenthesis(openN, closeN):
            if openN == closeN ==n:
                res.append("".join(stack))
                return
            if openN <n:
                stack.append("(")
                getParenthesis(openN+1, closeN)
                stack.pop()
            if closeN <openN:
                stack.append(")")
                getParenthesis(openN, closeN+1)
                stack.pop()
        
        getParenthesis(0,0)
        return res
     
        
