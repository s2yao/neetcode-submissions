class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        curr_posn = deque()
        for coin in coins:
            if coin == amount:
                return 1
            if coin < amount:
                curr_posn.append(coin)
        turns = 1
        visited = set()

        while curr_posn:
            curr_len = len(curr_posn)
            turns += 1

            for _ in range(curr_len):
                curr_amount = curr_posn.popleft()
                for coin in coins:
                    new_amount = curr_amount + coin
                    if new_amount in visited:
                        continue
                    visited.add(new_amount)
                    if new_amount == amount:
                        return turns
                    if new_amount < amount:
                        curr_posn.append(new_amount)
        
        return -1

