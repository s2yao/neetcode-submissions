class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)  == 2:
            return min(cost[1], cost[0])
        dp = [cost[0]] + [cost[1]] + [0] * (len(cost) - 2)

        for idx in range(2, len(cost)):
            if idx == (len(cost) - 1):
                dp[idx] = min(dp[idx - 2] + cost[idx], dp[idx - 1])
            else:
                dp[idx] = min(dp[idx - 2] + cost[idx], dp[idx - 1] + cost[idx])

        return dp[-1]