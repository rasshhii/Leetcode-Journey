class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # Calculate digit product
            prod = 1
            for digit in str(n):
                prod *= int(digit)
            
            # Check if product is divisible by t
            if prod % t == 0:
                return n
            
            n += 1