class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        
        def sort_diag(r, c):
            vals = []
            i, j = r, c
            while i < m and j < n:
                vals.append(mat[i][j])
                i += 1
                j += 1
            vals.sort()
            i, j = r, c
            idx = 0
            while i < m and j < n:
                mat[i][j] = vals[idx]
                idx += 1
                i += 1
                j += 1
        
        for r in range(m):
            sort_diag(r, 0)
        for c in range(1, n):
            sort_diag(0, c)
        
        return mat
