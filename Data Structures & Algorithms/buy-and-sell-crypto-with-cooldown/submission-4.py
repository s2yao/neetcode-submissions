from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0

        @cache
        def buy_sell_or_cooldown(idx, can_buy):
            if idx >= len(prices):
                return 0
            
            skip = buy_sell_or_cooldown(idx + 1, can_buy)

            if can_buy:
                buy = buy_sell_or_cooldown(idx + 1, False) - prices[idx]
                return max(buy, skip)
            else:
                sell = buy_sell_or_cooldown(idx + 2, True) + prices[idx]  
                return max(sell, skip)

        return buy_sell_or_cooldown(0, True)