class Solution:
    def deleteGreatestValue(self, grid):
        # Sort each row
        for row in grid:
            row.sort()
        
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        
        # Iterate column by column
        for col in range(cols):
            max_val = 0
            for row in range(rows):
                max_val = max(max_val, grid[row][col])
            total += max_val
        
        return total
