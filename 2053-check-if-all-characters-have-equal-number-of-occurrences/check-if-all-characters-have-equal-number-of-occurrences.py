class Solution:
    def areOccurrencesEqual(self, s):
        freq = {}
        
        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Get all frequencies
        values = list(freq.values())
        
        # Check if all frequencies are equal
        for v in values:
            if v != values[0]:
                return False
        
        return True
