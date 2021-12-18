#use two pointers to read two lists
#use one pointer to write in the nums1

#can't use the for i in (n) and for j in (m) because it will miss the 0s

#corner cases already considered in the function

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
      
                
        p1 = 0
        p2=0
        for i in range(m+n):
            if p2>= n or p1 <m and nums1_copy[p1]<=nums2[p2]: #two situations: 1. nums2 is shorter than nums1 and p2 already ran to the end of nums2
                                                                              #2. p1 <m and number in nums1 is smaller than number in nums2
                nums1[i] = nums1_copy[p1] # copy value
                p1+=1
        
            else:
                nums1[i] = nums2[p2]
                p2+=1
                
            
                
        return nums1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
