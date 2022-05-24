'''
Input: [3,2,1,5,6,4] and k = 2
Output: 5
'''

'''
This question has several ways to solve, the easies way is using heap, there is a built-in function heapq in Python
if without heapq function, we can initiaze a heap, and we keep puting new elements in the heap, if the size of the heap is larger than k, we pop, it will pop the smallest element
than means , we will always keep the k largest element in the heap, then we can peek it 
'''
class Solution(object):
    def findKthLargest(self, nums, k):
       
        return heapq.nlargest(k,nums)[-1]
'''
but it requires O(nlog(k)) 
'''

'''
Let's try a better way, quick sort
quick sort basically choosing a pivot and put all numbers smaller than the pivot to the left and larger to the right, and change the pivot every time to sort the array
since it requires partition while sorting, it is very efficient for kth smallest and largest question.
if we want kth smallest for a sorted array -> nums[k]
if we want kth largest for a sorted array -> nums[len(nums)-k]
so , in this question, we rewrite k = len(nums)-k

based on the logic behind quick sort, if our pivot was put in a position = len(nums)-k -> this is our answer, because we are sure there are k-1 element put on the right of it, ie, larger than it
so it should be the kth largest number 

'''

'''
思路：
let new k = len(nums) -k

then we write a helper function quickSort with input left pointer and right pointer to do the quick sort job 
and we will recurse this helper function by updating left and right

in the helper function
p = l -> we put our pointer to the left most position
pivot = nums[r] -> use right most position as pivot value, and the goal is to find position for this value
to iterate all values from l to r, w/ the right most, ie, the pivot
if the value is smaller than the pivot, we put it to the left, so we swap it with p, and we move pointer one step forward
then after we swap all values smaller than pivot, we make sure the pointer is pointing the position, where all values to the right are larger than the pivot
so we swap the pivot with the pointer
note, we don't care if left partition and right partition are sorted or not
at this point, if we have pointer position < new k, meaning our target value is on the right partition, so we redo the helper function for the right partition, other wise, left partition
if the pointer position = new k, this nums[p] is our answer
'''

class Solution(object):
    def findKthLargest(self, nums, k):
      k = len(nums)-1
      return self.quickSort(0,len(nums)-1,k,nums)
      
      
    def quickSort(self, l,r,k,nums):
      p = l
      pivot = nums[r]
      
      for i in range(l,r):
        if nums[i]<pivot:
          nums[i],nums[p] = nums[p],nums[i]
          p+=1
      nums[p], nums[r] = nums[r],nums[p]
      
      if p < k:
        return self.quickSort(p+1,r,k,nums)
      elif p>k:
        return self.quickSort(l,p-1,k,nums)
      else:
        return nums[p]
      

'''
Time Complexity : O(n)
Space Complexity : O(1)
'''








