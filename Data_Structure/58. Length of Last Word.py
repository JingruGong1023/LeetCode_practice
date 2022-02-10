class Solution(object):
    def lengthOfLastWord(self, s):
        lst = []
        lst = s.rstrip().split(" ")
        return len(lst[-1])
        """
        :type s: str
        :rtype: int
        """
        
