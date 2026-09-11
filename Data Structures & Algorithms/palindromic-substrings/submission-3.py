class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        # 2 ptr
        def is_palin(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1 
                r += 1

            return count
        
        for i in range(len(s)):
            ret += is_palin(i,i)
            ret += is_palin(i,i+1)

        return ret