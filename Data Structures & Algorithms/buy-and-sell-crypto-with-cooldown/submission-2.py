class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in reversed(range(n)):
            # Buy or skip
            dp[i][1] = max(
                dp[i + 1][0] - prices[i],
                dp[i + 1][1]
            )

            # Sell or skip
            dp[i][0] = max(
                dp[i + 2][1] + prices[i],
                dp[i + 1][0]
            )

        return dp[0][1]
