class Solution(object):
    def isPalindrome(self, s):
        
        if len(s)==0 or len(s)==1:
            return True
        
        s=''.join(e for e in s if e.isalnum())
        s = s.lower()
       
        if s == s[::-1]:
            return True
        else:
            return False
       
        
        """
        :type s: str
        :rtype: bool
        """
        
