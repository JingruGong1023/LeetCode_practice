'''
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

'''
Cannot use two pointers to loop through the array in N^2, it will exceed time limit
When come to two pointers, think of one pointer at the beginning, one pointer at the end when array sorted
'''

'''
思路：
two pointers for a sorted array, one(i) at the beginning, one(j) at the end
while i<j:
If their sum is bigger than the target - we move j to point to a smaller value
If their sum is smaller than the target - we move i to point to a larger value
otherwise, return i +1, j+1 (The question stated the index begins from 1)
'''

class Solution(object):
    def twoSum(self, numbers, target):
      i = 0
      j = len(numbers)-1
      while i <j:
        sum1 = numbers[i]+numbers[j]
        if sum1> target:
          j-=1
        elif sum1 <target:
          i+=1
        else:
          index1 = i+1
          index2 = j+1
          break
     return [index1,index2]

'''
Time Complexity : O(n)
Space Complexity: O(1)
'''
    
