class Solution:
    def stringSequence(self, target):
        result = []
        current = []
        
        for ch in target:
            # Press Key 1 (append 'a')
            current.append('a')
            result.append("".join(current))
            
            # Press Key 2 until last char becomes ch
            while current[-1] != ch:
                # Move to next character
                current[-1] = chr((ord(current[-1]) - ord('a') + 1) % 26 + ord('a'))
                result.append("".join(current))
        
        return result
