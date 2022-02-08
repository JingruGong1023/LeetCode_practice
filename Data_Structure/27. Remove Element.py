class Solution(object):
    def removeElement(self, nums, val):
        if val not in nums:
            return len(nums)
        
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
        
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
