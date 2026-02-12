class Solution:
    def freqAlphabets(self, s):
        result = ""
        i = 0
        
        while i < len(s):
            # Check if next pattern is like "10#"
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i+2])
                result += chr(ord('a') + num - 1)
                i += 3
            else:
                num = int(s[i])
                result += chr(ord('a') + num - 1)
                i += 1
        
        return result
