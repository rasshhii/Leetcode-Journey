class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k == 1:
            counts = Counter(nums)
            valid = [x for x, cnt in counts.items() if cnt == 1]
            return max(valid) if valid else -1
        
        if k == n:
            return max(nums)
            
        counts = Counter(nums)
        ans = -1
        
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans