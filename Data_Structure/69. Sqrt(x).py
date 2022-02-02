class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        left = 2
        right = x//2
        while left<=right:
            num = left+(right-left)//2
            
            if num**2 >x:
                right = num-1
            elif num**2<x:
                left= num+1
            else:
                return num
        return right
        """
        :type x: int
        :rtype: int
        """
        
