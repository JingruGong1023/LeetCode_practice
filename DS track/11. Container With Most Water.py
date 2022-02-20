class Solution(object):
    def maxArea(self, height):
        # brute force
        maxArea=0
        if height ==[] or len(height)==1:
            return 0
        
        #two pointers at the left and right endpoints of the list
        right = len(height)-1
        left = 0
        while right >left:
            h = min(height[right],height[left])
            w = right-left
            #print(h,w)
            maxArea = max(maxArea, h*w)
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
        return maxArea
            
        """
        :type height: List[int]
        :rtype: int
        """
        
