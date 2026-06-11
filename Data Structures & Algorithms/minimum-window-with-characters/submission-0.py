from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = defaultdict(int)
        window = defaultdict(int)

        # seed need
        for i in range(len(t)):
            need[t[i]] += 1

        # required character types
        required = len(need)

        # satisfied character types
        curr_satisfied = 0

        l = 0
        best_len = float("inf")
        best_l = best_r = 0

        # using window dict as sliding window
        for r in range(len(s)):
            # adding into window
            curr_char = s[r]

            # adding
            window[curr_char] += 1

            # check if current char just became satisfied
            if curr_char in need and need[curr_char] == window[curr_char]:
                curr_satisfied += 1

            # if current window is valid, keep shrinking from left
            while curr_satisfied == required:
                # update best window
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                    best_r = r

                # remove from window
                curr_remove = s[l]

                # check if removing this char will make window invalid
                if curr_remove in need and need[curr_remove] == window[curr_remove]:
                    curr_satisfied -= 1

                # removing
                window[curr_remove] -= 1
                l += 1

        if best_len == float("inf"):
            return ""

        return s[best_l:best_r + 1]