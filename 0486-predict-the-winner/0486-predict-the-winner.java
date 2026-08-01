class Solution {
    public boolean predictTheWinner(int[] nums) {
        final int n = nums.length;
        int[] dp = nums.clone();

        for (int d = 1; d < n; ++d) {
            for (int j = n - 1; j - d >= 0; --j) {
                int i = j - d;
                dp[j] = Math.max(nums[i] - dp[j],
                                 nums[j] - dp[j - 1]);
            }
        }

        return dp[n - 1] >= 0;
    }
}