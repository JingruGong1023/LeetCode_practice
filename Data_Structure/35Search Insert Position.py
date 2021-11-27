
class Solution(object):
    def searchInsert(self, nums, target):
       
        left = 0
        right = len(nums)-1
        
        while(left<=right): //only jump out of the loop when left > right
            mid = left+(right-left)//2 #to prevent overflow
            if nums[mid]<target: 
                left=mid+1  #the left bound is keeping updated 
            else:
                if nums[mid]==target:
                    return mid
                else:
                    right = mid-1 # in this case mid is impossible to be the desired position
        return left
            
                
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
