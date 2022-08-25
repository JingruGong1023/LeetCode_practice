'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
'''

'''
There are several things to notice
1. you cannot sort the array
2. the height of the rec is defined by the lower one
3. you cannot use brute force because it will exceed time limit
'''

'''
思路：
use two pointers
one on the left, one on the right, record the max area. and move the pointers inside
'''

class Solution(object):
    def maxArea(self, height):
        if len(height) ==2:
            return min(height[0],height[1])*1
        
        maxArea = 0
        l = 0
        r = len(height)-1
        
        while l<r:
            area = min(height[l],height[r])*(r-l)
            maxArea = max(area,maxArea)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxArea
            
        """
        time complexity: O(n)
        space complexity :O(1)
        """
