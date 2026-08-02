class Solution {

    private int[] piles;
    private int[][] dp;

    public boolean stoneGame(int[] piles) {
        this.piles = piles;
        int n = piles.length;
        dp = new int[n][n];

        return dfs(0, n - 1) > 0;
    }

    private int dfs(int left, int right) {
        if (left > right) {
            return 0;
        }

        if (dp[left][right] != 0) {
            return dp[left][right];
        }

        int chooseLeft = piles[left] - dfs(left + 1, right);
        int chooseRight = piles[right] - dfs(left, right - 1);

        dp[left][right] = Math.max(chooseLeft, chooseRight);

        return dp[left][right];
    }
}