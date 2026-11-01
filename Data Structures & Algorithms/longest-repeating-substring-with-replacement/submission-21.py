
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        curr_max = 0
        char_occ = defaultdict(int)
        ret = 0

        for right in range(len(s)):
            char_occ[s[right]] += 1
            curr_max = max(curr_max, char_occ[s[right]])

            window = right - left + 1 - curr_max
            if window > k:
                char_occ[s[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)

        return ret