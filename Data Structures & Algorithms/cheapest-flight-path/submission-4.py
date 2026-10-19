class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf")] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp_dp = dp.copy()

            for curr_airport, next_airport, cost in flights:
                if dp[curr_airport] == float('inf'):
                    continue
                
                if dp[curr_airport] + cost < temp_dp[next_airport]:
                    temp_dp[next_airport] = dp[curr_airport] + cost
            
            dp = temp_dp
        
        if dp[dst] == float('inf'): 
            return -1   
        return dp[dst]