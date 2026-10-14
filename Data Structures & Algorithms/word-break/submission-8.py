class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                curr_end = i + len(word)
                if curr_end <= len(s):
                    curr_chunk = s[i:curr_end]
                    if curr_chunk == word:
                        dp[i] = dp[curr_end]
                    if dp[i]:
                        break

        return dp[0]

