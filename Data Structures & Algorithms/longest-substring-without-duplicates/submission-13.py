class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # using a dictionary to record occurrence
        # but the curent char can still hit some characters before the current window

        left = 0 # updates to the current valid hit's last occurrence + 1
        ret = 0
        curr_duct = {}

        for right in range(len(s)):
            # hit
            if s[right] in curr_duct and curr_duct[s[right]] >= left:
                left = curr_duct[s[right]] + 1
            
            curr_duct[s[right]] = right
            ret = max(ret, right - left + 1)
        
        return ret