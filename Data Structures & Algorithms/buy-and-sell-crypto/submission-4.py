class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        curr_max = prices[-1]

        for i in reversed(range(len(prices))):
            if prices[i] > curr_max:
                curr_max = prices[i]
            else:
                ret = max(ret, curr_max - prices[i])

        return ret

# [5,1,5,6,7,1]
# ret = 1
# curr = 7
