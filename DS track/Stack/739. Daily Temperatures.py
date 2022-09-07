'''
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''

'''
For this question, the most obvious solution is loop through the remaining list to find a larger temp for each element in the list
However, it will cost us O(n2) time
So we can use stack to save some time
The basic logic would be: while we adding element to the stack, once we found a larger temp, we pop the previous one until it is not larger than stack.pop
'''

'''
create a stack to store the element as well as its index, create a list of 0 with the length of input to store the output => incase we cannot find warmer day
for element in temperatures:
while stack is not empty and element > the last element of stack:
   we get index and value from the stack.pop
   res[index] = index of the element - index => the difference in days the temperature gets warmer
stack append element and its index => so we can find the result for this element

return res
'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = []
        
        for i, e in enumerate(temperatures):
            while stack and e > stack[-1][1]:
                index, value = stack.pop()
                res[index] = i - index
            stack.append([i,e])
        return res
                
        
        """
        Time Complexity :O(n)
        Space Complexity :O(n)
        """
