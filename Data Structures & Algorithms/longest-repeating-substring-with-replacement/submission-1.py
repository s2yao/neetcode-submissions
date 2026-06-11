from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        # dictionary to record frequency
        freq = defaultdict(int)
        max_freq = 0
        ret = 0

        # sliding window left boundary
        left = 0

        for right in range(len(s)):
            # expand window: include s[right]
            freq[s[right]] += 1

            # update max_freq (do NOT recompute max(freq.values()) each time)
            max_freq = max(max_freq, freq[s[right]])

            # if replacements needed > k, shrink from the left
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # window is valid here
            ret = max(ret, right - left + 1)

        return ret
