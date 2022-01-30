class Solution(object):
    def climbStairs(self, n):
        a = 1
        b =1
        for _ in range(n-1):
            a,b = a+b,a
        return a
        """
        :type n: int
        :rtype: int
        """
        
