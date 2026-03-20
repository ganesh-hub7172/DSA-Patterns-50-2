import bisect

class Solution:
    def maximumCount(self, nums):
        # First index where number >= 0
        first_non_negative = bisect.bisect_left(nums, 0)
        
        # First index where number > 0
        first_positive = bisect.bisect_right(nums, 0)
        
        neg = first_non_negative
        pos = len(nums) - first_positive
        
        return max(neg, pos)