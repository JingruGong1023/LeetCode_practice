class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0]=1
            row[-1]=1
            
            for j in range(1,len(row)-1):
                row[j] = triangle[i-1][j-1]+triangle[i-1][j]
            
            triangle.append(row)
            
        return triangle
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        """
        Dynamic Programmin
        base case: the beginning and the end element for each row is 1
        recursive case: element is equal to sum of two element in the above row
        Time complexity : O(numRows^2)
