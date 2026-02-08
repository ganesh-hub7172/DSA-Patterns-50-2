class Solution:
    def findMissingElements(self, nums):
        s = set(nums)
        lo = min(nums)
        hi = max(nums)

        res = []
        for x in range(lo + 1, hi):
            if x not in s:
                res.append(x)

        return res
