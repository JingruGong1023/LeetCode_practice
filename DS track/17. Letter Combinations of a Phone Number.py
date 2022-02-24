class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
         # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = ['']
        for d in digits:
            tmp = []
            for y in result:
                for x in letters[d]:
                    tmp.append(y+x)
            result = tmp
        
        return result
        """
        :type digits: str
        :rtype: List[str]
        """
       
