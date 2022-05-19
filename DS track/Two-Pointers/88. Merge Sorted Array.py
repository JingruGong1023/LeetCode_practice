'''
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

'''
1. we need to put pointers at the end of two arrays, and begin update from the end of nums1, otherwise while we update the values in nums1, the original value will be replaced
2. consider the case nums2 has more values
'''

'''
思路：
we have two non decreasing sorted array, we need to update nums1. since non decreasing, we update from the end, which is , finding the largest value first
let i = m-1, j= n-1, and end = m+n-1 -> the position update in nums1
while i and j non negative -> we loop the largest common number of values in the two arrays, 
if nums1[i]>nums2[j] -> update nums1[end] with nums1[i] -> put the larger value in the later position , then update end and i
else -> update nums1[end] with nums2[j] -> put the larger value in the later position , then update end and j

so it is possible after the loop, we will have some values in nums1 or nums2 not be ordered yet
if j >=0 -> means we still have values in nums2, and they should be smaller than all the values compared already
so put it at the beginning of nums1 
if we still have values left in nums1, we don't need to do anything to deal with them, because they are smaller than the values compared already, and they are expected to stay at the beginning
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #edge case:
        if not nums2:
            return nums1
        i = m-1
        j = n-1
        end = m+n -1
        
        while i >=0 and j>=0:
          if nums1[i]>nums2[j]:
            nums1[end]= nums1[i]
            end-=1
            i-=1
          else:
            nums1[end] = nums2[j]
            end-=1
            j-=1
        
        if j >=0:
          nums1[:end+1] = nums2[:j+1]
 
'''
Time Complexity : O(n)
Space Complexity : O(1)
'''

