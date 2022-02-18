class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        #we will have two pointers, prev and cur
        #prev+1<= cur-1 we add the range [prev+1,cur-1]
        result = []
        
        #edge cases 
        if nums ==[]:
            if lower <upper:
                result.append(str(lower)+"->"+str(upper))
                return result
            elif lower ==upper:
                result.append(str(lower))
                return result
            
        
        if nums[0]> lower:
            prev = lower-1
        else:
            prev = lower
        
        if nums[-1]< upper:
            nums.append(upper+1) 
        else:
            nums.append(upper) 
        
        for i in range(len(nums)):
            cur = nums[i]
            if prev +1<cur-1:
                result.append(str(prev+1)+"->"+str(cur-1))
            elif prev+1==cur-1:
                result.append(str(prev+1))
            prev = cur
        return result
        
        
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        Time Complexity :O(N)
        Space Complexity: O(1)
        """
        
