class Solution:
    def minSteps(self, s, t):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for ch in t:
            cnt[ord(ch) - ord('a')] -= 1

        steps = 0
        for x in cnt:
            if x > 0:
                steps += x

        return steps
