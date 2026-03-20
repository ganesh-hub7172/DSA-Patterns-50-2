class Solution:
    def rangeAddQueries(self, n, queries):
        # Step 1: Create matrix
        mat = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Step 2: Apply difference updates
        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            if c2 + 1 < n:
                mat[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                mat[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                mat[r2 + 1][c2 + 1] += 1
        
        # Step 3: Prefix sum (row-wise)
        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
        
        # Step 4: Prefix sum (column-wise)
        for j in range(n):
            for i in range(1, n):
                mat[i][j] += mat[i - 1][j]
        
        # Step 5: Trim to n x n
        return [row[:n] for row in mat[:n]]