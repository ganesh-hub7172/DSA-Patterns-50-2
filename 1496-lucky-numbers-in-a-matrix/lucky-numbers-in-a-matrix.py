class Solution:
    def luckyNumbers(self, matrix):
        # Minimum of each row
        row_mins = [min(row) for row in matrix]
        
        # Maximum of each column
        col_maxs = [max(col) for col in zip(*matrix)]
        
        result = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                    result.append(matrix[i][j])
        
        return result
