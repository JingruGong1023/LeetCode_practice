class Solution(object):
    def removeDuplicates(self, nums):
        count =1
        i=1
        while i <len(nums):
            if nums[i] ==nums[i-1]:
                count+=1
                if count>2:
                    nums.pop(i)
                    i-=1
            else:
                count=1
            i+=1
        
        return len(nums)
                
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Time Complexity :O(N^2)
        Space complexity : O(1)
