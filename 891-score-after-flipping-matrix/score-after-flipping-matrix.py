class Solution:
    def matrixScore(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        score = 0
        
        # First column (most significant bit)
        score += m * (1 << (n - 1))
        
        # Remaining columns
        for j in range(1, n):
            ones = 0
            
            for i in range(m):
                # If row was flipped (grid[i][0] == 0),
                # current value becomes flipped
                if grid[i][0] == 1:
                    ones += grid[i][j]
                else:
                    ones += 1 - grid[i][j]
            
            # Choose max between flipping column or not
            ones = max(ones, m - ones)
            
            score += ones * (1 << (n - j - 1))
        
        return score
