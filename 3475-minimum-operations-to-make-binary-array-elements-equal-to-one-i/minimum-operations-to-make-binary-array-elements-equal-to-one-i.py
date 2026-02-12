class Solution:
    def minOperations(self, nums):
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):
            if nums[i] == 0:
                # Flip next 3 elements
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                operations += 1
        
        # After processing, check last two elements
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        
        return operations
