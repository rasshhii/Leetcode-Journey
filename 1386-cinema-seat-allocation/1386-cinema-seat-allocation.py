class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                seats[r] |= (1 << (c - 2))
        
        ans = (n - len(seats)) * 2
        
        for mask in seats.values():
            left = (mask & 0b00001111) == 0
            right = (mask & 0b11110000) == 0
            middle = (mask & 0b00111100) == 0
            
            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
                
        return ans