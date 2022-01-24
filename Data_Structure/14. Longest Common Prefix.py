class Solution(object):
    def longestCommonPrefix(self, strs):
        sz=zip(*strs)
        result = ""
        for element in sz:
            if len(set(element))>1:
                break;
            result+=element[0]
        return result
        """
        :type strs: List[str]
        :rtype: str
        """
      
        
