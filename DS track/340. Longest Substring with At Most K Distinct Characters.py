class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        map = collections.defaultdict(int) #if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created
        i = 0
        ans = 0
        n = len(s)
        for j in range(n):
            map[s[j]]+=1
            while len(map)>k:
                map[s[i]]-=1
                if map[s[i]]==0:
                    del map[s[i]]
                i+=1
            ans = max(ans, j-i+1)
        return ans
        """
        :type s: str
        :type k: int
        :rtype: int
        """
       
