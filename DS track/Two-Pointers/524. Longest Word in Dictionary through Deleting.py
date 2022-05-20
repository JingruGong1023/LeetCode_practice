'''
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

'''

'''
1. way to order string by both alphabetic and length : min(s1,s2,key = lambda x: (-len(x),x)) -> there is "-" in len(x) because that means we want the longer word
2. the whole idea of this question is to use two pointers, one to loop the string, another one to loop the word in the dictionary
if after we loop through the string, there is some char in word that not pointed, the word is not a subset of the string
3. use helper function to check the subset, use outer function to sort
'''

'''
思路：
two pointers: i , j , intialize as 0 -> i loop through s , j loop through each word in dictionary
helper function to check if subset: while i <len(s) and j <len(word) 
if s[i] == word[j] -> j+=1
i+=1 no matter what
out of the while function, check if j = len(word)
outer function:
for each word in d -> if helper function returns True, we check if this word is smaller alphabetic and longer in length than previous result, if so, update result
'''

class Solution(object):
    def findLongestWord(self, s, dictionary):
      if not s or not dictionary:
        return ""
      
      result = ""
      for char in dictionary:
        if self.isSubset(char, s):
          result = min(char,result, key = lambda x: (-len(x),x))
      return result 
    
    #helper function
    def isSubset(self,sub, whole):
      n,m= len(sub),len(whole)
      i,j = 0,0
      
      while i <n and j < m:
        if sub[i] == whole[j]:
          i+=1
        j+=1
      return i == n
  

'''
Time Complexity : O(mn)
Space Complexity : O(1)
'''
      
      
      
      
      
      
      
      
      
