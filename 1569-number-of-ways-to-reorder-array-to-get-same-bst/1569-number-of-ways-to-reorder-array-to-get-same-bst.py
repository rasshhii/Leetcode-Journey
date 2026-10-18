from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left_ways = dfs(left)
            right_ways = dfs(right)

            return (comb(len(left) + len(right), len(left)) * left_ways * right_ways) % MOD

        return (dfs(nums) - 1) % MOD