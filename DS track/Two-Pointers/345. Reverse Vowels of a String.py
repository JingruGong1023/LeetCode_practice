'''
Given s = "leetcode", return "leotcede".
'''

'''
One thing to notice that, when create a list of vowels, remember to include both lower case and upper case
convert string to list: list(s)
convert list to string: ''.join(s)
be sure to assign s[j] and s[i] to cj and ci variables, instead of let s[i] = s[j], s[j]=s[i], it won't reverse successfully
'''

'''
思路：
create a list of all vowels
two pointers : i = 0, j = len(s)-1
change s to list s.t we can change the elements in s (string type is immutable)
while i <j:
if both i and j in vowels -> exchange, i+=1,j-=1 <- remember this!
if only i in vowels: j-=1
if only j in vowels: i+=1
return ''.join(s)
'''

class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        i = 0
        j = len(s)-1
        s = list(s)
        
        while i <j:
          ci = s[i]
          cj = s[j]
          if (ci in vowels) and (cj in vowels):
            s[i] = cj
            s[j] = ci
            j-=1
            i+=1
          elif (ci in vowels) and (cj not in vowels):
            j-=1
          else:
            i+=1
        
      return ''.join(s)
    
'''
Time Complexity : O(n)
Space Complexity : O(1)
'''
           
