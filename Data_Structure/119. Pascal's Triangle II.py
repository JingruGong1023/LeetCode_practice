class Solution(object):
    def getRow(self, rowIndex):
        ans = [1]*(rowIndex+1);
        up = rowIndex
        down = 1
        for i in range(1, rowIndex):
            ans[i] = ans[i-1]*up/down;
            up = up - 1
            down = down + 1
        return ans;
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
