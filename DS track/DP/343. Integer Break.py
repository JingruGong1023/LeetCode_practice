'''
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
'''

'''
The key problem here is we might have different product, but we want the max one
How can we break down a large integer, it based on how did we break down a smaller one
so it's a dp problem
'''

'''
思路
define dp
dp[i] is the max product number i can get
initialize dp
dp[1] = 1
dp[2] = 1
define equation
dp[i] = max(dp[i],max(dp[j]*(i-j),(i-j)*j))
define loop
for i in range(3,n+1):
  for j in range(2,i):
'''

class Solution(object):
    def integerBreak(self, n):
        dp = [0]*(n+1)
        
        dp[2] = 1
        
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(dp[j]*(i-j),j*(i-j)))
        return dp[-1]
        
        
        """
        Time Complexity : o(N)
        Space Complexity : o(N)
        """
        
  
