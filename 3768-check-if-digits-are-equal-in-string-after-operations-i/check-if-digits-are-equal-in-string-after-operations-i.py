class Solution:
    def hasSameDigits(self, s):
        while len(s) > 2:
            nxt = []
            for i in range(len(s) - 1):
                nxt.append(str((int(s[i]) + int(s[i + 1])) % 10))
            s = "".join(nxt)

        return s[0] == s[1]
