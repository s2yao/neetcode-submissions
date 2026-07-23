class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def dfs(start, arr):
            if start == len(s):
                ret.append(arr[:])
                return
            
            curr_str = ""
            for idx in range(start, len(s)):
                string = s[idx]
                curr_str += string
                if check(curr_str):
                    arr.append(curr_str)
                    dfs(idx + 1, arr)
                    arr.pop()

        def check(arr):
            for i in range(len(arr) // 2):
                left_idx = i
                right_idx = len(arr) - 1 - i
                if arr[left_idx] != arr[right_idx]:
                    return False
            return True
        
        dfs(0, [])
        return ret

