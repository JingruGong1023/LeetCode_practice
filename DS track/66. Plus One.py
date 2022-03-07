class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return
        n = len(digits)
        for i in range(n):
            idx = n - 1- i #get the last digit
            if digits[idx]==9:
                digits[idx]=0
            else:
                digits[idx]+=1
                return digits
            
        return [1]+digits
            
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
