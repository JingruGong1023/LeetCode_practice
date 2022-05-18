'''
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
'''

'''
Similar as TwoSum II, two pointers to find the sum of squares
The key is to avoid looping through all values from 0 to a large integer, we need to find a smaller ceiling
which could be sqrt(target)
'''

'''
思路：
edge case:
target < 0 -> False
two pointers : i = 0, j = sqrt(target) - if not integer, get its floor
while i <= j: here we have = because it is possible target = ssq of two equal int
if sum of squares two pointers > target - move j to point a smaller value
if sum of squares two pointers < target - move i to point a larger value
else:
return True
'''

class Solution(object):
    def judgeSquareSum(self, c):
      if c <0:
        return False
      i = 0
      j = floor(math.sqrt(c))
      
      while i <= j:
        sum1 = i**2+j**2
        if sum1 > c:
          j-=1
        elif sum1 < c:
          i+=1
        else:
          return True
      
      return False

'''
Time Complexity : O(n)
Space Complexity : O(1)

