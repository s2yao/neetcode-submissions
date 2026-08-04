class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new_dict = defaultdict(int)
            for val, count in dp.items():
                new_dict[val + num] += count
                new_dict[val - num] += count
            dp = new_dict

        return dp[target]