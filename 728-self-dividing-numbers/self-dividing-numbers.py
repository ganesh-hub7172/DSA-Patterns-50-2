class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        
        for num in range(left, right + 1):
            valid = True
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    valid = False
                    break
            if valid:
                result.append(num)
        
        return result
