'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

'''
the hard point with this problem is , the first solution normally we will think of is looking at every substring and record the length of the ones without repeat char
but it will result in O(n^2)
To avoid this, we should find a way to look less substrings.
for sliding window, we always need to think about the idea that there are some windows/elements we already looked and we don't need to include them into the next window
'''

'''
思路：
for this question,
when we reached 'abca', there is a duplicate 'a', we remove the first 'a'
move the window to 'bcab', we remove the first 'b'
move the window to 'cabc', we remove the first 'c'
move the window to 'abcb', noticed here, we have the duplicate b in the second position, so we need to remove both 'a' and 'b'
move the window to 'abb', remove both 'a' and 'b'
record the length and compare
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        maxLength = 0
        seen = set()
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxLength = max(r-l+1, maxLength)
        return maxLength
        
                
        """
        Time Complexity :O(n)
        Space Complexity : O(n)
        """
