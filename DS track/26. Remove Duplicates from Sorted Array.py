class Solution(object):
    def removeDuplicates(self, nums):
        if set(nums)==nums:
            return len(nums)
        
        seen = set()
        i = len(nums)-1
        while i>=0:
            if nums[i] not in seen:
                seen.add(nums[i])
                #print(seen)
                i-=1
            else:
                nums.pop(i)
                i-=1
                
       
        """
        :type nums: List[int]
        :rtype: int
        """
        
