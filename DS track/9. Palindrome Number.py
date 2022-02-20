class Solution(object):
    def isPalindrome(self, x):
        if x <0:
            return False
        if x>0 and x%10 ==0:
            return False
        original = x
        result = 0
        #reverse the number
        while x>0:
            result = result*10+x%10
            x=x//10
        #print(result)
        
        return original==result
        
        
        
        """
        :type x: int
        :rtype: bool
        """
   
