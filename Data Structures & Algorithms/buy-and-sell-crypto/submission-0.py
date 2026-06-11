class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        ret_max = 0

        for i in range(len(prices) - 1):
            curr_max = prices[i + 1] - prices[i]
            # if curr_max > 0:
            ret = max(0, curr_max + ret)
            ret_max = max(ret_max, ret)
        return ret_max