class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        if min_val % 2 != 0:
            return True
        
        min_odd = float('inf')
        for x in nums1:
            if x % 2 != 0 and x < min_odd:
                min_odd = x
        
        if min_odd == float('inf'):
            return True
        
        for x in nums1:
            if x % 2 != 0 and x - min_odd <= 0:
                return False
                
        return True
        