class Solution(object):
  #recursive
    def plusOne(self, digits):
        if len(digits)==1 and digits[0]==9:
            return [1,0]
        if digits[-1]!= 9:
            digits[-1]+=1
            return digits
        else:
            digits[-1]=0
            digits[:-1]=self.plusOne(digits[:-1])
            return digits
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
       
  #Iterative
   def plusOne(self, digits):
        n = len(digits)
        for i in range(n):
            idx = n-i-1 #move from backwards
            if digits[idx] ==9:
                digits[idx]=0
            else:
                digits[idx]+=1
                return digits
        return [1]+digits
                
            
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
