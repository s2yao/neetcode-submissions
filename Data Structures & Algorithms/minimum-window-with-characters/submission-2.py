from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # using 2 dictionary to record s and t
        need = defaultdict(int)
        window = defaultdict(int)

        # seed need
        for ele in t:
            need[ele] += 1
        
        # condition for deciding current window
        # while required == curr_satisfy
        required = len(need)
        curr_satisfy = 0

        # keep track of current min window
        min_l = min_right = 0
        curr_min_ret = float("inf")

        l = 0

        for right in range(len(s)):
            curr_ele = s[right]
            window[curr_ele] += 1
            # check if some element satisfied
            if (curr_ele in need) and (need[curr_ele] == window[curr_ele]):
                curr_satisfy += 1
            
            # if current window contains every character of t
            while curr_satisfy == required:
                curr_ele_left = s[l]

                if window[curr_ele_left] == need[curr_ele_left]:
                    # by removing this element it can make window invalid
                    # record down current valid window
                    if right - l + 1 < curr_min_ret:
                        min_l = l
                        min_right = right
                        curr_min_ret = right - l + 1
                    curr_satisfy -= 1
                window[curr_ele_left] -= 1
                l += 1
        
        if curr_min_ret == float("inf"):
            return ""


        return s[min_l:min_right + 1]
            
        