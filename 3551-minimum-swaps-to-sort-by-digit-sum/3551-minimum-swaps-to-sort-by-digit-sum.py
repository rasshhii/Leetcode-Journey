class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n):
            return sum(int(d) for d in str(n))

        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        indexed_nums.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or indexed_nums[i][1] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = indexed_nums[j][1]
                cycle_size += 1

            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps