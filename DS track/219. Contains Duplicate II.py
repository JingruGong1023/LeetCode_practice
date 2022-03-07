class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if not nums:
            return False
        
        dic ={}
        
        for i , v in enumerate(nums):
            if v in dic and abs(i-dic[v])<=k:
                return True
            dic[v]=i
        
        return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
