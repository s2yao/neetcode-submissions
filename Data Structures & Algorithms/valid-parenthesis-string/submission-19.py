from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs_backtrack(idx, left_bracket, right_bracket):
            if right_bracket > left_bracket:
                return False
            if idx == len(s):
                if left_bracket == right_bracket:
                    return True
                else:
                    return False
            
            ret = False
            if s[idx] == '(':
                result_left = dfs_backtrack(idx + 1, left_bracket + 1, right_bracket)
                ret = ret or result_left
            elif s[idx] == ')':
                result_right = dfs_backtrack(idx + 1, left_bracket, right_bracket + 1)
                ret = ret or result_right
            else:
                as_left = dfs_backtrack(idx + 1, left_bracket + 1, right_bracket)
                as_right = dfs_backtrack(idx + 1, left_bracket, right_bracket + 1)
                as_empty = dfs_backtrack(idx + 1, left_bracket, right_bracket)

                ret = as_left or as_right or as_empty
            
            return ret
        
        return dfs_backtrack(0, 0, 0)
