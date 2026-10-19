class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        word_set = set(wordDict)

        for i in reversed(range(len(s))):
            for word in wordDict:
                end_idx = i + len(word)
                if end_idx > len(s):
                    continue
                curr_window = s[i:end_idx]
                if curr_window == word:
                    dp[i] = dp[i] or dp[end_idx]

        return dp[0]