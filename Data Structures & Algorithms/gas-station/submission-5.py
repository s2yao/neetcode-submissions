class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res








        # O(n^2)


        # curr_gas = 0
        # def test_if_work(idx, end_idx, curr_gas):
        #     if idx == len(gas):
        #         return test_if_work(0, end_idx, curr_gas)
        #     if cost[idx] > (gas[idx] + curr_gas):
        #         return False
        #     if idx == end_idx:
        #         return True
        #     return test_if_work(idx + 1, end_idx, gas[idx] + curr_gas - cost[idx])

        # # start from every station
        # for station in range(len(gas)):
        #     if gas[station] < cost[station]:
        #         continue
        #     if test_if_work(station + 1, station, gas[station] - cost[station]):
        #         return station
        
        # return -1

    

