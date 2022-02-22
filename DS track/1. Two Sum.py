class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return []
        result = []
        for i in range(len(nums)-1):
            prev = nums[i]
            nxt = target - prev
            for j in range(i+1,len(nums)):
                if nums[j] ==nxt:
                    result=[i,j]
                    return result
            
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
