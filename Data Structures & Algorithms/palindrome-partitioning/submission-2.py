class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_palin(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        curr = []
        ret = []

        def backtrack(idx):
            if idx == len(s):
                ret.append(curr.copy())
                return
            
            for i in range(idx, len(s)):
                if not check_palin(idx, i):
                    continue
                curr.append(s[idx: i + 1])
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return ret