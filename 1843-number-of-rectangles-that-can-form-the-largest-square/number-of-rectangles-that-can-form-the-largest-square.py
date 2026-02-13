class Solution:
    def countGoodRectangles(self, rectangles):
        maxLen = 0
        
        # Find maximum possible square side
        for l, w in rectangles:
            maxLen = max(maxLen, min(l, w))
        
        count = 0
        
        # Count rectangles that can form square of size maxLen
        for l, w in rectangles:
            if min(l, w) == maxLen:
                count += 1
        
        return count
