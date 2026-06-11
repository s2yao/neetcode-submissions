class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using a hash map to store most ocurred char
        occur_dict = defaultdict(int)
        ret = 0
        left = 0
        curr_max = 0
        
        for right in range(len(s)):
            occur_dict[s[right]] += 1

            curr_max = max(curr_max, occur_dict[s[right]])

            if (right - left + 1) - curr_max > k:
                occur_dict[s[left]] -= 1
                left += 1
            
            ret = max(ret, right - left + 1)

        return ret
                