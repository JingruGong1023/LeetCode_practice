'''
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

'''
This question will use sliding windows
we will use two pointers for this question
slow pointer will point to the beginning index, fast pointer will point to the ending index
begin with slow = fast = 0
'''

'''
思路：
slow = fast = 0
edge case: len nums = 1 and nums[0] <target: return 0 else 1
res = float('inf) define a large value for the min length we want to find
define a sum to record our sum
for fast in len nums:
sum+=nums[fast]
while the value sums >= target , record the min length, delete the value nums[slow] from sum and slow move forward
out of the while loop, means our sum <target, fast move forward
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        s =0
        if len(nums)==1:
            if nums[0]<target:
                return 0
            else:
                return 1
            
        res = float('inf')
        sum1 = 0
        for f in range(len(nums)):
            sum1+=nums[f]
            while sum1 >= target:
                res = min(res, (f-s+1))
                sum1-=nums[s]
                s+=1
            
            
        return 0 if res == float('inf') else res
                
                
        """
       Time Complexity: O(n)
       Space Complexity : O(1)
        """
        
