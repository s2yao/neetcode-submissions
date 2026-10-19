from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def backtrack(day, can_buy):
            if day >= len(prices):
                return 0
            
            curr_max = 0
            skip = backtrack(day + 1, can_buy)
            curr_max = max(curr_max, skip)

            if can_buy:
                buy = backtrack(day + 1, False) - prices[day]
                curr_max = max(curr_max, buy)
            else:
                sell = backtrack(day + 2, True) + prices[day]
                curr_max = max(curr_max, sell)
            return curr_max
        
        return backtrack(0, True)