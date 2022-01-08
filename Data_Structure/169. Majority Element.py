class Solution(object):
    def majorityElement(self, nums):
        if len(nums)==1:
            return nums[0]
        
        majority = len(nums)//2
        
        for element in set(nums):
            if nums.count(element) >majority:
                return element
            
        return -1
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
