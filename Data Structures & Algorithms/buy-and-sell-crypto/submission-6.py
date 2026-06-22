class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ret = 0
        curr_max_price = 0

        for price in reversed(prices):
            if curr_max_price < price:
                curr_max_price = price
            else:
                max_ret = max(max_ret, curr_max_price - price)
        
        return max_ret