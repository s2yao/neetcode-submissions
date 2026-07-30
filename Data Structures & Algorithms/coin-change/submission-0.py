class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        seen = [False] * amount
        queue = deque([0])
        ret = 0

        while queue:
            ret += 1
            curr_lvl = len(queue)

            for i in range(curr_lvl):
                curr_val = queue.popleft()
                for coin in coins:
                    if coin + curr_val == amount:
                        return ret
                    
                    if coin + curr_val > amount or seen[coin + curr_val]:
                        continue
                    
                    seen[coin + curr_val] = True
                    queue.append(coin + curr_val)
        
        return -1
