from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        curr = []

        def check_palin(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        @cache
        def backtrack(idx, curr):
            if idx == len(s):
                ret.append(list(curr))
                return
            
            for i in range(idx, len(s)):
                if not check_palin(idx, i):
                    continue
                
                backtrack(i + 1, curr + (s[idx:i+1],))
        
        backtrack(0, ())
        return ret