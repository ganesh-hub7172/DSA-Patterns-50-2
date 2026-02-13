class Solution:
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)
        
        # Euclidean algorithm
        while largest != 0:
            smallest, largest = largest, smallest % largest
        
        return smallest
