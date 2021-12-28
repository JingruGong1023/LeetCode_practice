#Using sorted, O(nlogn)
class Solution(object):
    def isAnagram(self, s, t):
        result = False
        if len(s)!= len(t):
            return False
        
       
        
            
        if sorted(s)==sorted(t):
            result = True
        
        return result
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
 #Using dictionary O(n)
class Solution(object):
    def isAnagram(self, s, t):
        result = True
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for k in t:
            if k not in dic: #means there is some char in t but not in s
                result = False
            else:
                dic[k]-=1 #if they have the same number for char k, it will ==0 for the key
        
        for i in dic.values():
            if i != 0:
                result= False
            
        
        return result
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
