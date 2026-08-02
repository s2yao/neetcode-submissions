class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] * (amount + 1)
        process = [0]

        ret = 0
        while process:
            next_lvl = []
            ret += 1
            for curr_ele in process:
                for coin in coins:
                    reach = curr_ele + coin
                    if reach > amount or dp[reach] != 0:
                        continue
                    if reach == amount:
                        return ret
                    dp[reach] = ret
                    next_lvl.append(reach)
            process = next_lvl

        return -1

# coins = [2], amount = 3
# ret = 1
# dp = [0010]
# process = []
# next_lvl = [2]
# reach = 0 + 2