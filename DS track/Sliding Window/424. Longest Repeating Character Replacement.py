'''
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''

'''
For this question, we need to pay attention that our first intuitive might be checking every substring, but this will result in O(n2) time complexity
So what should we do?
First, we need to determine which char in the string to be replaced, though this is not required, but it will help us keep track if the replacement is legal
For example, in the substring, 'ABA' , A has the largest count, so obviously we won't touch it, we should change B. But how should we know the replacement is legal
since we can only replace k char, if a substring contains more than k chars that need to be replaced, it is illegal. We check this by length of substring - max count of char in the substring <=k
if it is illegal, we move our window
'''

'''
思路：
record the count of each char in a dictionary
let left pointer l = 0
loop through the string
check if the substring replacement is legal
if it is, record the length
while it is not, meaning, if we add the s[r], there will be more than k chars need to be replaced
drop the char in the window from the left until droped s[r]
'''

class Solution(object):
    def characterReplacement(self, s, k):
        if not s:
            return 0
        if len(s)==1:
            return 1
        
        res = 0
        count={}
        l = 0
        
        for r in range(len(s)):
            count[s[r]] =1+count.get(s[r],0)
            while (r-l+1)-max(count.values()) >k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
        
        """
       Time Complexity : o(n)
       space complexity : o(n)
        """
