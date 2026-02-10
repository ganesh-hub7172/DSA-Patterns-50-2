class Solution:
    def thirdMax(self, nums):
        distinct = set(nums)

        if len(distinct) < 3:
            return max(distinct)

        distinct.remove(max(distinct))
        distinct.remove(max(distinct))
        return max(distinct)
