'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

'''
need to notice that we may have more than one list in the answer, and result lists cannot be duplicate
so we should create a set to store the result lists to avoid duplicity
since the target is 0, we can think of this as similar as two sum, the only difference is we need to identify the first number first, then use the tech in 2sum to find the remaining numbers
Also notice, it returns number, not index
'''

'''
思路：
define a result as set()
sort the list
loop through the list, in the loop, create j = i+1, k = len(nums)-1, our target should be find nums[j]+nums[k]=-nums[i]
if we find nums[j]+nums[k]<-nums[i], then j+=1, nums[j]+nums[k]>-nums[i], then k-=1, else, found one possible answer, add it to the set, and k-=1, j+=1
out of the loop: return result
'''

class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return
        if len(nums)<3 or (len(nums)==3 and sum(nums)!=0):
            return 
        res = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j <k:
                if nums[j]+nums[k] < -nums[i]:
                    j+=1
                elif nums[j]+nums[k] > -nums[i]:
                    k-=1
                else:
                    res.add((nums[i],nums[j],nums[k]))
                    k-=1
                    j+=1
            
        return res
        
        
        
        """
        Time Complexity :O(n2)
        Space Complexity : from \mathcal{O}(\log{n})O(logn) to \mathcal{O}(n)O(n), depending on the implementation of the sorting algorithm. 
        """
        
        
   
