class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            key = nums[i]
            j = i-1
            while j>=0 and key<nums[j]:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key
        
        result = False
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                result = True
        return result
        """
        :type nums: List[int]
        :rtype: bool
        """
        
