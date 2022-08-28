'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
'''

'''
The key to this problem is we cannot use brute force, otherwise we will face time limit exceeds
we should think of a way that can avoid searching through all the elements in the matrix
'''

'''
思路:
we search from the bottom left. so that if our target is larger than the element, we can move a step right, otherwise we move a step up.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix[0][0]>target:
            return False
        if matrix[-1][-1]<target:
            return False
        
        #search from the bottom left
        row = len(matrix)-1
        col = 0
        
        while col < len(matrix[0]) and row >=0:
            if target > matrix[row][col]:
                col+=1
            elif target < matrix[row][col]:
                row -=1
            else:
                return True
        
        return False
                               
        """
        Time complexity : O(n+m)
        space complexity : o(1)
        """
        
                               
        
