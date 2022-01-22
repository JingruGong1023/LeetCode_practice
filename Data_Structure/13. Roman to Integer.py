class Solution(object):
    def romanToInt(self, s):
        values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "Z":0}
        ans =0
        s=s+'Z'
        for i in range(len(s)-1):
            if values[s[i]] >= values[s[i+1]]:
                ans+= values[s[i]]
            else:
                ans -=values[s[i]]
        
        return ans
        
        """
        :type s: str
        :rtype: int
        """
        
