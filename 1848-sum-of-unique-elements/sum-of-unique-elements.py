class Solution:
    def sumOfUnique(self, nums):
        freq = {}
        
        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        total = 0
        
        # Sum elements that appear exactly once
        for num in freq:
            if freq[num] == 1:
                total += num
        
        return total
