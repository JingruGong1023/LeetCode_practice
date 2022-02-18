class Solution(object):
    def summaryRanges(self, nums):
        result = []
        #edge case
        if nums==[]:
            return []
        
        prev = nums[0]
        nums.append(nums[-1]+2)
        for i in range(len(nums)-1):
            cur = nums[i]
            nxt = nums[i+1]
            if cur+1<= nxt-1:
                if prev==cur:
                    result.append(str(prev))
                else:
                    result.append(str(prev)+"->"+str(cur))
                prev =nxt
            
            else:
                
                continue
        return result
        
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
