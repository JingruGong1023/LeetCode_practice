class Solution(object):
    def rotate(self, matrix):
        l = 0
        r = len(matrix)-1
        while l<r:
            matrix[l],matrix[r] = matrix[r],matrix[l]
            l+=1
            r-=1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
        
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        SELECT invoice_id, customer_name, price, COUNT(contact_name) OVER(PARTITION BY c.user_id) as contact_cnt, 
