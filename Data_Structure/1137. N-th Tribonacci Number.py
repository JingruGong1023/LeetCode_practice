class Solution(object):
    def tribonacci(self, n):
        if n ==0:
            return 0
        if n==1:
            return 1
        if n ==2:
            return 1
        a = 0
        b=1
        c=1
        for _ in range(n-2):
            a,b,c = b,c,a+b+c
            
        return c
        """
        :type n: int
        :rtype: int
        """
        
