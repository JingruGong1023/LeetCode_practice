class Solution(object):
    def longestPalindrome(self, s):
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s,i,i)
            p2=self.get_palindrome(s,i,i+1)
            p = max(p,p1,p2, key = lambda x:len(x))
        return p
        
    def get_palindrome(self,s,l,r):
        while l>= 0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
        
        """
        :type s: str
        :rtype: str
        """
        
        
