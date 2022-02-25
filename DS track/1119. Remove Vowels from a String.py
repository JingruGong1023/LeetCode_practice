class Solution(object):
    def removeVowels(self, s):
        if not s:
            return ""
        
        vowls = ['a','e','i','o','u']
        
        result = ""
        
        for i in range(len(s)):
            if s[i] not in vowls:
                result = result + s[i]
        
        return result
            
        """
        :type s: str
        :rtype: str
        """
        
