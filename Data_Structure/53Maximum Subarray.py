class Solution(object):
    def maxSubArray(self, nums):
        curNum = nums[0]
        maxNum = nums[0]
        for i in range(1,len(nums)):
            if curNum<0:
                curNum = 0
            curNum = curNum+nums[i]
            if curNum>maxNum:
                maxNum = curNum
            
        return maxNum
        """
        :type nums: List[int]
        :rtype: int
        """
        
#Dynamic Programming, Kadane's Algorithm
#Whenever see a question that asks max or min of something, Dynamic programming is possible. 
#Divide the problem into smaller and easier sub questions. 
#TIME COMPLEXITY: O(n)
#SPACE COMPLEXITY: O(1): no matter how long the input is, we are only using 2 variables
