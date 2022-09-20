'''
Input: m = 3, n = 7
Output: 28
'''

'''
思路：
Firstly, this question is walking through a board, a matrix
so we need to initialize dp as matrix as well
1. define dp
dp[i][j] is the number of unique paths achieving at board[i][j] location
2. initialize dp
dp[i][0] = 1 - only 1 possible path to arrive any point at first col
similarly dp[0][j] = 1

3. define equation 
we know that to get to some point, we two possible directions, go to right, or go to bottom
which means, the total possible path to achieve board[i][j] could be equal to the total path go to board[i-1][j] plus the total path go to board[i][j-1]
dp[i][j] = dp[i-1][j]+dp[i][j-1]
4 decide looping path
we need to loop through all rows then cols
5. define return
we need to return the total unique path ahieving right bottom of the board, ie, the last col and last row
so we need to return dp[-1][-1]
'''

class Solution(object):
    def uniquePaths(self, m, n):
        
        dp= [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                #print(dp)
                
        return dp[-1][-1]
        """
        Time complexity : O(mn)
        Space complexity :O(mn)
        """
        
