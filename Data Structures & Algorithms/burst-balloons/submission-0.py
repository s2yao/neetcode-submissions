class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        m = len(arr)
        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                best = 0
                for k in range(i + 1, j):
                    coins = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                    if coins > best:
                        best = coins
                dp[i][j] = best

        return dp[0][m - 1]