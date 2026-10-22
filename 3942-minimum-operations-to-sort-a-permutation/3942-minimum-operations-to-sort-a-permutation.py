class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        idx = [0] * n
        for i, val in enumerate(nums):
            idx[val] = i

        is_inc = True
        for i in range(n):
            if (nums[i] - nums[i - 1]) % n != 1:
                is_inc = False
                break

        is_dec = True
        for i in range(n):
            if (nums[i - 1] - nums[i]) % n != 1:
                is_dec = False
                break

        if not is_inc and not is_dec:
            return -1

        ans = float("inf")
        idx0 = idx[0]

        if is_inc:
            ans = min(ans, idx0)
            ans = min(ans, 2 + (n - idx0) % n)

        if is_dec:
            ans = min(ans, 1 + (idx0 + 1) % n)
            ans = min(ans, 1 + (n - 1 - idx0))

        return ans