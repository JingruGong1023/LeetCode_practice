'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
'''

'''
restriction: O(n) time complexity, no division
so we couldn't write two nested loops to calculate the product. 
The hard part is that we need to figure out a way to get right side and left side numbers without nested loop of the list
'''

'''
思路：
edge case: if not nums: return
create list Results to store and update the products
1. we get the right side and left side numbers in two recursions
2. for left side:
  let results[0] = 1
  loop through index 1 to length of the list, update results[i] = nums[i-1]*results[i-1]
  here, results[i-1] stores the product of all numbers on the left side of nums[i-1], all we need to do is multiply by nums[i-1]
3. for right side
  create variable R = 1, as indicate the right side of the rightmost number(which is nothing)-> times 1 = times nothing
  loop through index length of the list to 0 -> reversed
  update results[i] = results[i]*R, R*= nums[i]
  here results[i] stores all values product of left side of nums[i], R stores all values product of the right side of nums[i]
'''

class Solution(object):
    def productExceptSelf(self, nums):
        
        if not nums:
            return
         
        results = []
        results[0] = 1
        for i in range(1,len(nums)):
          results[i] = results[i-1]*nums[i-1]
         
        R = 1
        for i in reversed(range(len(nums))):
          results[i] = results[i]*R
          R *= nums[i]
        
        return results
                          
        
        
        
        
        
        
  
