class Solution(object):
    def twoSumLessThanK(self, nums, k):
        if not nums:
            return -1
        
        maxSum=0
        for i in range(len(nums)-1):
            num1 = nums[i]
            for j in range(i+1,len(nums)):
                num2 = nums[j]
                if num1+num2<k:
                    maxSum = max(maxSum, num1+num2)
                
                    
        return maxSum if maxSum !=0 else -1
                    
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
