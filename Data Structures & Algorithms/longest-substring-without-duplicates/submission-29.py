class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_char = defaultdict(int)
        left = 0
        ret = 0

        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in dict_char and dict_char[curr_char] >= left:
                left = dict_char[curr_char] + 1
            ret = max(ret, right - left + 1)
            dict_char[curr_char] = right
        
        return ret