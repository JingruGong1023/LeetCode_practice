class Solution(object):
    def titleToNumber(self, columnTitle):
        n=len(columnTitle)
        number = 0
        
        for i in range(len(columnTitle)):
            number = number*26
            number += (ord(columnTitle[i])-ord('A')+1)
        return number
        """
        :type columnTitle: str
        :rtype: int
        """
        
