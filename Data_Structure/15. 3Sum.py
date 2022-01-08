class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        
        if len(nums) <3 or nums[0]>0:
            return []
       
        
        result = set()
        
        for i in range(len(nums)):
            target = 0-nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    result.add((nums[i],nums[r],nums[l]))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        
        return list(result)
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        """
        Time Complexity: O(n2)
        Space Complexity : O(n)
        """
        
