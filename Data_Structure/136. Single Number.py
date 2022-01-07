class Solution(object):
    def singleNumber(self, nums):
        seen = set()
        seen.add(nums[0])
        for i in range(1,len(nums)):
            if nums[i] in seen:
                seen.remove(nums[i])
            else:
                seen.add(nums[i])
        return seen.pop()
            
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Time Complexity:
        O(n)
        """
