class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dict_occ = defaultdict(int)
        ret = 0


        for right in range(len(s)):
            dict_occ[s[right]] += 1

            # check curr window if over k replacement
            max_occ = max(dict_occ.values())
            remain = (right - left + 1) - max_occ
            if remain > k:
                dict_occ[s[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)
        
        return ret