class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0

        # let a dictionary record occurrence

        curr_dict = defaultdict(int)

        # we use a sliding window 
        left = 0
        
        # we need the formula: (right - left + 1) - most_occur > k
        # to judge if current sliding window is valid
        most_occur = 1

        ret = 0

        for right in range(len(s)):
            # update dict
            curr_dict[s[right]] += 1

            most_occur = max(most_occur, curr_dict[s[right]])
            
            # update left until the current window is valid
            while (right - left + 1) - most_occur > k:
                curr_dict[s[left]] -= 1
                left += 1

            ret = max(ret, (right - left + 1))
        
        return ret

s="AABABBA"
k=1