class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        m = min(strs)
        M = max(strs)
        
        for i, letter in enumerate(m):
            if letter != M[i]:
                return m[:i]
        return m

        """
        :type strs: List[str]
        :rtype: str
        """
