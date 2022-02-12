class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(set(s)) ==1:
            return 1
        
        n = len(s)
        ans = 0 #store the current max length
        
        map = {} #store the current position of each char
        
        i = 0
        for j in range(n):
            if s[j] in map:
                i = max(map[s[j]],i) #move the beginning index of the longest substring to the next unique char
            ans = max(ans, j-i+1)
            map[s[j]] = j+1 #so that when update, i will go to the next unique char instead of the existed char
        
        return ans
                
        
        """
        :type s: str
        :rtype: int
        """
        
