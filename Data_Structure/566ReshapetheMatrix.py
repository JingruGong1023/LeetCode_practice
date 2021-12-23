class Solution(object):
    def matrixReshape(self, mat, r, c):
        matrix = []
        row = []
        
        #corner case
        if len(mat)==0 :
            return mat
        
        #put all items in a list first
        for i in mat:
            for j in i:
                row.append(j)
                
        #construct the matrix
        if len(row)!= r*c:
            return mat
        else:
            for i in range(0, len(row),c):
                matrix.append(row[i:i+c])
            return matrix
        
        
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        
