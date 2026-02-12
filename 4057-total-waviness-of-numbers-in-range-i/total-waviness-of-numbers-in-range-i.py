class Solution:
    def totalWaviness(self, num1, num2):
        total = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            
            if len(s) < 3:
                continue
            
            for i in range(1, len(s) - 1):
                if (s[i] > s[i-1] and s[i] > s[i+1]) or \
                   (s[i] < s[i-1] and s[i] < s[i+1]):
                    total += 1
        
        return total
