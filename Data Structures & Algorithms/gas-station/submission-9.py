class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        have_gas = 0
        curr_ret = 0
        for idx, (curr_gas, curr_cost) in enumerate(zip(gas, cost)):
            have_gas += curr_gas - curr_cost
            if have_gas < 0:
                curr_ret = idx + 1
                have_gas = 0
                
        return curr_ret