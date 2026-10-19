class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dict_occ = defaultdict(int)
        ret = 0

        for right in range(len(s)):
            curr_char = s[right]
            dict_occ[curr_char] += 1

            max_occ = max(dict_occ.values())

            while left < right and (right - left + 1) - max_occ > k:
                left_char = s[left]
                dict_occ[left_char] -= 1
                if not dict_occ[left_char]:
                    del dict_occ[left_char]
                max_occ = max(dict_occ.values())
                left += 1
            
            ret = max(ret, right - left + 1)
        
        return ret