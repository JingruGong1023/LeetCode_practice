class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums)==3:
            return nums[0]+nums[1]+nums[2]
        if len(nums)<3:
            return 
        
        nums.sort()
        minSum = nums[0]+nums[1]+nums[2]
       
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                sum1 = nums[i]+nums[l]+nums[r]
                if sum1 == target:
                    return sum1
                if abs(sum1-target) <abs(minSum-target):
                    minSum = sum1
                if sum1 <target:
                    l+=1
                elif sum1>target:
                    r-=1
        
        return minSum
       
            
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
