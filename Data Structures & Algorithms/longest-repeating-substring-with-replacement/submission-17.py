class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dict_occ = defaultdict(int)
        ret = 0

        def get_max(dictionary):
            curr_val = 0
            curr_key = 0
            for key, val in dictionary.items():
                if val > curr_val:
                    curr_val = val
                    curr_key = key
            
            return [curr_key, curr_val]

        for right in range(len(s)):
            curr_char = s[right]
            dict_occ[curr_char] += 1

            max_char, max_occ = get_max(dict_occ)

            while left < right and (right - left + 1) - max_occ > k:
                left_char = s[left]
                dict_occ[left_char] -= 1
                if not dict_occ[left_char]:
                    del dict_occ[left_char]
                max_char, max_occ = get_max(dict_occ)
                left += 1
            
            ret = max(ret, right - left + 1)
        
        return ret