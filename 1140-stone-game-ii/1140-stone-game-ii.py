class Solution:

    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        dp = {}

        def get_max(i: int, m: int) -> int:
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]
            if (i, m) in dp:
                return dp[(i, m)]

            max_stones = 0
            for x in range(1, 2 * m + 1):
                # Opponent's best turn from (i + x) leaves us suffix_sum[i + x] - get_max(i + x, max(m, x))
                max_stones = max(
                    max_stones,
                    suffix_sum[i] - get_max(i + x, max(m, x)),
                )

            dp[(i, m)] = max_stones
            return max_stones

        return get_max(0, 1)