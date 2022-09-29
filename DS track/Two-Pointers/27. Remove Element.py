'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

'''
Two pointers
slow point to the index of new array
fast point to the index as we check the older array
'''

'''
思路：
slow =0
fast = len(nums)-1
while slow<fast:
if we find slow point to target, we replace the value slow pointed to with the value fast point to , and fast move backward
because fast might point to target as well
out of the if loop, means we already replace slow value with a non target value, we move slow one step ahead
and continue the loop
return slow
'''
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        if len(nums)==1:
            return 0 if nums[0] == val else 1
        s = 0
        f = len(nums)-1
        
        while s <= f:
            if nums[s] == val :
                nums[s] = nums[f]
                f-=1
            #print(f)
            else:
                s+=1
            
        return s
        
        
        """
        Time complexity : O(n)
        Space Complexity : O(1)
        """
        
