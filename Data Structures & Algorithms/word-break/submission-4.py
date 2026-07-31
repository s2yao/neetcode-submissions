class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for idx in range(len(s) - 1, -1, -1):
            for word in wordDict:
                end_idx = idx + len(word)
                # print(end_idx)
                if end_idx <= len(s):
                    curr_word = s[idx:end_idx]
                    if curr_word == word:
                        dp[idx] = dp[idx + len(word)]
                        if idx == 0 and dp[0]:
                            return True
                # print(dp)
        
        return dp[0]

# s="abcd"
# wordDict=["a","abc","b","cd"]
# 00101
# idx = 2
