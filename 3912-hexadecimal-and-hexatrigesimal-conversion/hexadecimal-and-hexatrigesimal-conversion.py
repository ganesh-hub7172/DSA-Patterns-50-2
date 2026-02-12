class Solution:
    def concatHex36(self, n):
        # Convert number to given base
        def convert(num, base):
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if num == 0:
                return "0"
            
            result = ""
            while num > 0:
                result = chars[num % base] + result
                num //= base
            return result
        
        square_hex = convert(n * n, 16)
        cube_36 = convert(n * n * n, 36)
        
        return square_hex + cube_36
