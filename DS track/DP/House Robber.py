'''
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4
'''

'''
思路：
1. define dp
dp[i] means the most amount of money you can rub at house i
2. define equation
dp[i] = max(dp[:i-1])+nums[i]
3. define loop
we need to loop throught the nums
4. initialize dp
dp[0] = nums[0]
dp[1] = nums[1]
5. edge case
if len nums ==1:
return num[0]
if len nums ==2:
return max(nums)
'''

class Solution(object):
    def rob(self, nums):
        dp = [0]*len(nums)
        
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2,len(nums)):
            dt = dp[:(i-1)]
            dp[i] = max(dt)+nums[i]
        
        return max(dp)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
