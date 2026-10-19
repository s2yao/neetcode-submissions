class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        left = 0
        dict_last_occ = defaultdict(int)

        for right in range(len(s)):
            if s[right] in dict_last_occ:
                if dict_last_occ[s[right]] >= left:
                    left = dict_last_occ[s[right]] + 1
            
            dict_last_occ[s[right]] = right
            ret = max(right - left + 1, ret)

        return ret