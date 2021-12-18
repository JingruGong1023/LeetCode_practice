'''
Used Binary search in this question
Firstly, sort two arrays, then use two pointers p1 and p2 to compare two arrays
if number in nums1 is smaller than number in nums2, p1 move forward one step, otherwise p2 move forward one step
if two numbers are the same, append the number in the result array
Since once the two numbers are the same, both pointers move forward, avoid the situation that counting the times the number appears wrong
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        p1=0
        p2=0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]==nums2[p2]:
                result.append(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
            
        return result
        
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
