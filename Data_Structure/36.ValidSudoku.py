class Solution(object):
    def isValidSudoku(self, board):
        result = True
        box = [set() for _ in range(9)]
        #check rows
        for i in range(9):
            row = board[i]
            rowCheck = []
            for j in range(9):
                if row[j] in rowCheck and row[j]!=".":
                    result = False
                rowCheck.append(row[j])
            
        
        
        #check columns
        for col in zip(*board):
            colCheck = []
            for j in range(9):
                if col[j] in colCheck and col[j]!=".":
                    result = False
                colCheck.append(col[j])
        
        #square check
        for i in range(9):
           
            for j in range(9):
                val = board[i][j]
                idx = (i//3)*3+(j//3)
                if val in box[idx] and val!=".":
                    result = False
                box[idx].add(val)
        
        return result
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
