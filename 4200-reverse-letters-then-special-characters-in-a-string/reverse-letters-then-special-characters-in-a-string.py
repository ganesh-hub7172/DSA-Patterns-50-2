class Solution:
    def reverseByType(self, s):
        letters = []
        special = []
        
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)
        
        letters.reverse()
        special.reverse()
        
        result = []
        i = 0
        j = 0
        
        for ch in s:
            if ch.isalpha():
                result.append(letters[i])
                i += 1
            else:
                result.append(special[j])
                j += 1
        
        return "".join(result)
