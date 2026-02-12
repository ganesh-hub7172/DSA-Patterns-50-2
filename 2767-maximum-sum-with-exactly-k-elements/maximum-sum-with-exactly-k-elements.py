import heapq

class Solution:
    def maximizeSum(self, nums, k):
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        score = 0
        
        for _ in range(k):
            m = -heapq.heappop(heap)
            score += m
            heapq.heappush(heap, -(m + 1))
        
        return score
