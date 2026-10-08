class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dict_char = defaultdict(int)
        ret = 0
        curr_window = 0

        for i in range(len(s)):
            curr_char = s[i]

            if curr_char in dict_char:
                distance = i - dict_char[curr_char]
                curr_window = min(curr_window + 1, distance)
            else:
                curr_window += 1

            ret = max(ret, curr_window)
            dict_char[curr_char] = i

        return ret