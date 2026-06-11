class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        
        # we use a dict to record
        curr_dict = defaultdict(int)

        # sliding window
        left = 0

        ret = 0

        # most_occured variable in the window
        most_occured = 1

        for right in range(len(s)):
            # add to the dictionary
            curr_dict[s[right]] += 1

            # update the most_occured
            most_occured = max(most_occured, curr_dict[s[right]])

            # while the current window is invalid
            while (right - left + 1) - most_occured > k:
                curr_dict[s[left]] -= 1
                left += 1
            
            # up to this point, sliding window must be valid
            # update ret
            ret = max(ret, right - left + 1)
        
        return ret

                

