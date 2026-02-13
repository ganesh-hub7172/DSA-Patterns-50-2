class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}
        
        # Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Find maximum frequency
        max_freq = max(freq.values())
        
        # Sum frequencies of elements having maximum frequency
        total = 0
        for count in freq.values():
            if count == max_freq:
                total += count
        
        return total
