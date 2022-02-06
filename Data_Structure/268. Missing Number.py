class Solution(object):
    def missingNumber(self, nums):
        diff = 0
        for i in range(len(nums)):
            diff+= nums[i]-i
        return len(nums)-diff
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
