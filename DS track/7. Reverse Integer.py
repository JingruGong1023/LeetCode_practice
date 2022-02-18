class Solution(object):
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: return 0
        
        str_x= str(abs(x))
        str_reverse = str_x[::-1]
        
        
        if x >0:
            str_reverse= int(str_reverse)
        else:
            str_reverse= -int(str_reverse)
            
        if str_reverse>= 2**31-1 or str_reverse <= -2**31: return 0
        else:
            return str_reverse
                
            
        """
        :type x: int
        :rtype: int
        """
        
