class Solution(object):
    def findTheDifference(self, s, t):
        if s =="":
            return t
        
        sortedS = sorted(s)
        sortedT = sorted(t)
        
        i = 0
        while i <len(s):
            if sortedS[i]!=sortedT[i]:
                return sortedT[i]
            i+=1
        return sortedT[i]
        
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
