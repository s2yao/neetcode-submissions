class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)  == 2:
            return min(cost[1], cost[0])
        dp0 = cost[0]
        dp1 = cost[1]

        for idx in range(2, len(cost)):
            temp = dp1
            if idx == (len(cost) - 1):
                dp1 = min(dp0 + cost[idx], temp)
            else:
                dp1 = min(dp0 + cost[idx], temp + cost[idx])
            dp0 = temp

        return dp1