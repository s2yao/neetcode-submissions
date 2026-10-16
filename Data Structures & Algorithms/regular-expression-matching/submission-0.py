from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def backtrack(i, j):
            # Pattern exhausted
            if j == len(p):
                return i == len(s)

            # Check whether current characters match
            match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # Next character is *
            if j + 1 < len(p) and p[j + 1] == "*":

                # Option 1: Skip x* entirely (zero occurrences)
                skip = backtrack(i, j + 2)

                # Option 2: Consume one character, keep x*
                take = match and backtrack(i + 1, j)

                return skip or take

            # Normal character or .
            return match and backtrack(i + 1, j + 1)

        return backtrack(0, 0)