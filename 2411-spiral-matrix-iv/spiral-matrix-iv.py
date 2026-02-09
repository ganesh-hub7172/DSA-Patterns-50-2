class Solution:
    def spiralMatrix(self, m, n, head):
        res = [[-1] * n for _ in range(m)]
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        curr = head
        
        while curr and top <= bottom and left <= right:
            for j in range(left, right + 1):
                if not curr: return res
                res[top][j] = curr.val
                curr = curr.next
            top += 1
            
            for i in range(top, bottom + 1):
                if not curr: return res
                res[i][right] = curr.val
                curr = curr.next
            right -= 1
            
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if not curr: return res
                    res[bottom][j] = curr.val
                    curr = curr.next
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if not curr: return res
                    res[i][left] = curr.val
                    curr = curr.next
                left += 1
        
        return res
