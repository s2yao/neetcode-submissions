class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [-1] * n
        dp[src] = 0

        # preprocess inputs as start, end, weight
        
        for _ in range(k + 1):
            temp_dp = dp.copy()

            for start, end, cost in flights:
                if dp[start] == -1:
                    continue
                if temp_dp[end] == -1:
                    temp_dp[end] = dp[start] + cost
                else:
                    temp_dp[end] = min(temp_dp[end], dp[start] + cost)
            
            dp = temp_dp

        if dp[dst] == -1:
            return -1
        
        return dp[dst]