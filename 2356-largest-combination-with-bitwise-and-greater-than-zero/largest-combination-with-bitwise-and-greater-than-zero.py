class Solution:
    def largestCombination(self, candidates):
        max_count = 0
        
        for bit in range(32):  # check 32 bits
            count = 0
            for num in candidates:
                if num & (1 << bit):
                    count += 1
            max_count = max(max_count, count)
        
        return max_count
