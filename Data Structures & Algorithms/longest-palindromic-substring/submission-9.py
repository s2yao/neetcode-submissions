class Solution:
    def longestPalindrome(self, s: str) -> str:
        def detect(l, r):
            ret = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            
            return s[l+1:r]

        result = ""
        curr_max = 0
        for i in range(len(s)):
            odd = detect(i, i)            
            even = detect(i, i+1)

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
            
        return result
            
