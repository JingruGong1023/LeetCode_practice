class Solution(object):
    def merge(self, intervals):
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        stack = []
        
        for interval in intervals:
            if not stack or stack[-1][1]<interval[0]:
                    stack.append(interval)
            else:
                    stack[-1][1] = max(stack[-1][1],interval[1])
        return stack
            
                
                    
        
        
        
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
