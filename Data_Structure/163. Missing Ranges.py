class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        prev = lower -1 #to handle case when nums is empty
        
        for i in range(len(nums)+1):
            cur = nums[i] if i <len(nums) else upper+1
            if cur >prev+1:
                if prev+1<cur-1:
                    res.append(str(prev+1)+"->"+str(cur-1)) 
                else:
                    res.append(str(prev+1)) #deal with the equality
            prev = cur
        return res
                    
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        Time complexity : O(n)
        Space Complexity has the worst case O(n) but output space that is simply used to return the output (and not to do any processing) 
        is not counted for the purpose of space complexity analysis. For this reason, the overall space complexity is O(1).
        """
        
