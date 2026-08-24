class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        num = len(word2)
        for col in range(len(word2) + 1):
            dp[len(word1)][col] = num
            num -= 1
        
        num = len(word1)
        for row in range(len(word1) + 1):
            dp[row][len(word2)] = num
            num -= 1
        
        for row in reversed(range(len(word1))):
            for col in reversed(range(len(word2))):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row + 1][col + 1]
                else:
                    replace = dp[row + 1][col + 1]
                    delete_word2 = dp[row][col + 1]
                    insert_word2 = dp[row + 1][col]
                    dp[row][col] = 1 + min(replace, delete_word2, insert_word2)
        
        print(dp)
        return dp[0][0]


