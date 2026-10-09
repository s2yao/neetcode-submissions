class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        left = 0
        dict_last_occ = defaultdict(int)

        for right in range(len(s)):
            curr_char = s[right] 
            if curr_char in dict_last_occ:
                last_idx = dict_last_occ[s[right]]
                left = max(left, last_idx + 1)
            dict_last_occ[s[right]] = right
            ret = max(ret, right - left + 1)
        
        return ret 