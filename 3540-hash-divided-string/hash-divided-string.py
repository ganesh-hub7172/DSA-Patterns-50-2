class Solution:
    def stringHash(self, s, k):
        res = []
        
        for i in range(0, len(s), k):
            total = 0
            for ch in s[i:i+k]:
                total += ord(ch) - ord('a')
            res.append(chr((total % 26) + ord('a')))
        
        return "".join(res)
