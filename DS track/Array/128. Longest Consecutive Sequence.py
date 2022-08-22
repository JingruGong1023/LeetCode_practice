'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
'''
The idea here is create different sequences for the list
count the length every sequence of the consecutive numbers
The problem is how do we know it's the start and the end of the sequence
'''
        
'''
思路：
create a set of nums
for each number of the nums, if there is no number -1 exist in the set, it means it is the beginning of some sequence. so we begins from here, with this number, while there exists number + length in the set, we add 1 to the length.
in the end, compare length and the longest
'''

class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        
        longest = 0
        length = 0
        for n in nums:
          if n-1 not in numset:
            length = 1
            while n+length in numset:
              length +=1
          longest = max(length, longest)
        return longest
      
'''
Time complexity: O(n)
Space complexity: O(n)
'''
