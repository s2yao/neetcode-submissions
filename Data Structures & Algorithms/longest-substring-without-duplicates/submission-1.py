class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dictionary to record 
        # all the current encountered elements with index
        curr_dict = defaultdict(int)

        # sliding window to record down the currently unrepeated string
        
        left = 0
        ret = 0

        for right in range(len(s)):
            # if dup found
            if s[right] in curr_dict:
                # update left to be current idx + 1
                # be careful of referencing earlier character
                left = max(curr_dict[s[right]] + 1, left)
            
            # update
            curr_dict[s[right]] = right

            ret = max(ret, right - left + 1)

        return ret
    
# s="abc!abcbb"
# left = 0
# ret = 3
# dict = {a:0, b:1, c:3, }