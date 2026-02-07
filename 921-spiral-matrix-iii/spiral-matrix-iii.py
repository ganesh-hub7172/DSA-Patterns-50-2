class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        res = []
        total = rows * cols
        
        r, c = rStart, cStart
        res.append([r, c])
        
        step = 1
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # east, south, west, north
        
        while len(res) < total:
            for i in range(4):
                dr, dc = dirs[i]
                moves = step
                for _ in range(moves):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                if i == 1 or i == 3:
                    step += 1
        
        return res
