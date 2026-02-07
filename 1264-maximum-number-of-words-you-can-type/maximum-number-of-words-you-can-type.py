class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        broken = set(brokenLetters)
        count = 0
        
        for word in text.split():
            ok = True
            for ch in word:
                if ch in broken:
                    ok = False
                    break
            if ok:
                count += 1
        
        return count
