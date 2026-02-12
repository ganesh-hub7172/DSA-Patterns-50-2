class Solution:
    def countSquares(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        total = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = 1 + min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    )
                total += matrix[i][j]
        
        return total
