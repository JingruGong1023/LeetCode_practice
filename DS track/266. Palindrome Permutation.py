class Solution(object):
    def canPermutePalindrome(self, s):
        #if s length is even, every character in the string must always occur an even number of times.
        #if s length is odd, every character except one of the characters must always occur an even number of times
        
        if len(s) ==1:
            return True
        
        result = {}
        for i in range(len(s)):
            if s[i] in result:
                result[s[i]] +=1
            else:
                result[s[i]] =1
        
        #we don't need to split the situation for even and odd length, because if there is only one char in even number with odd count, the length won't be even
        count = 0
        for values in result.values():
            if values%2:
                count+=1
            if count >1:
                return False
        return True
            
            
        
        """
        :type s: str
        :rtype: bool
        """
        
