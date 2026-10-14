class Solution:
    def numDecodings(self, s: str) -> int:
        prev1 = 1
        prev2 = 0

        for i in reversed(range(len(s))):
            curr = 0
            if s[i] != '0':
                curr += prev1
                if i + 2 <= len(s) and "10" <= s[i:i+2] <= "26":
                    curr += prev2
            prev2 = prev1
            prev1 = curr
        
        return curr