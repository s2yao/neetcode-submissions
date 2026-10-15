class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for coin in coins:
            for i in range(amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
