class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)  == 2:
            return min(cost[1], cost[0])
        dp0 = cost[0]
        dp1 = cost[1]

        for idx in range(2, len(cost)):
            temp = dp1
            dp1 = cost[idx] + min(temp, dp0)
            dp0 = temp

        return min(dp1, dp0)
