class Solution(object):
    def sortColors(self, nums):
        zero = 0
        one = 0
        two = 0
        for element in nums:
            if element == 0:
                zero+=1
            if element == 1:
                one+=1
            if element ==2:
                two +=1
        
        for i in range(zero):
            nums[i] = 0
        firstTwo = zero+one
        for i in range(zero,firstTwo):
            nums[i]=1
        for i in range(firstTwo,len(nums)):
            nums[i]=2
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
