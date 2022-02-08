class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==1 and nums[0]==0:
            return nums
      
        for i in range(len(nums)):
            if nums[i]==0 :
                
                nums.append(0)
                nums.remove(0)#remove the first zero found (from left)
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
