class Solution:
    def minimumPushes(self, word):
        from collections import Counter
        
        freq = Counter(word)
        counts = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        for i in range(len(counts)):
            pushes = (i // 8) + 1
            total_pushes += counts[i] * pushes
        
        return total_pushes
