class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        word_set = set(wordDict)
        all_len = [len(word) for word in wordDict]

        for i in reversed(range(len(s))):
            for curr_len in all_len:
                end_idx = i + curr_len
                if end_idx > len(s):
                    continue
                if s[i:end_idx] in word_set:
                    dp[i] = dp[i] or dp[end_idx]



            # for word in wordDict:
            #     end_idx = i + len(word)
            #     if end_idx > len(s):
            #         continue
            #     curr_window = s[i:end_idx]
            #     if curr_window == word:
            #         dp[i] = dp[i] or dp[end_idx]

        return dp[0]