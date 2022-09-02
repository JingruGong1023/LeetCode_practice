'''
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
'''

'''
The trick is to understand permutation.
We say string1 is a permutation of string2 if and only if the count of each char in two strings are the same
so we only need to check if there is one substring in s2 contains the same count of chars as in s1
we will achive this by creating two counter dics, one for s1 and one for sliding window
'''

'''
思路：
'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        if not s2:
            return False
        
        d1 = {x:s1.count(x) for x in s1}
        window = s2[:len(s1)]
        d2 = {x:window.count(x) for x in window}
        
        if d1==d2:
            return True
        
        for i in range(len(s2)-len(s1)):
            if d2[s2[i]] ==1:
                del d2[s2[i]]
            elif d2[s2[i]] >1:
                d2[s2[i]]-=1
            
            d2[s2[len(s1)+i]]= d2.get(s2[len(s1)+i],0)+1
            if d1==d2:
                return True
        return False
                
