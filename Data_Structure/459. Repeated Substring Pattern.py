class Solution(object):
    def repeatedSubstringPattern(self, s):
        if len(s)<=1:
            return False
        ss = (s+s)[1:-1]
        return ss.find(s) != -1
            
        """
        :type s: str
        :rtype: bool
        """
        
