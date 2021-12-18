class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target and i != j:
                    output.append(i)
                    output.append(j)
                    return output
                
        
