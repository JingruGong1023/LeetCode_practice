'''
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''

'''
remove a character from string:
1. s1 = s.replace(char, "")
2. s[:pos]+s[pos+1:]

recursion: add another function -> make it parallel to the original function

valid a palindrome: two pointers equal from beginning and end
The main problem in this question is to delete one possible character from the string and make it palindrome
we need to notice that, it is possible we do not need to delete anything
while we comparing two pointers, if they are not equal , we delete either one, and see if it is a palindrome
we don't need to deal with the whole string, since we already compare all chars other than those between the pointers
so we can do s[i:j] to delete j or s[i+1:j+1] to delete i

'''

'''
思路：
a helper function: ispalindrome(S) to validate a palindrome
two pointers: i , j
if s[i]==s[j] -> i+=1, j-=1 keep going
otherwise, we delete one char, and check with the helper function, if the remaining is palindrome, return true, otherwise False
if we didn't return anything and the loop stops, we return True, that means the original string is a palindrome
'''

class Solution(object):
    def validPalindrome(self, s):
      #edge case:
      if len(s) ==1:
        return True
      i = 0
      j = len(s) -1
      
      while i <j:
        if s[i]==s[j]:
          i+=1
          j-=1
        else:
          return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])
      
      return True
    def isPalindrome(s):
      return s==s[::-1]

'''
Time complexity: O(n)
Space complexity : O(1)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
