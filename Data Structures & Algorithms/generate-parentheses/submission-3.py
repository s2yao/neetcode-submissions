class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        ret = []

        def backtrack(left, right):
            if left + right == n * 2:
                ret.append("".join(curr))
                return
            
            if left < n:
                curr.append("(")
                backtrack(left + 1, right)
                curr.pop()
            
            if right < left:
                curr.append(")")
                backtrack(left, right + 1)
                curr.pop()
        
        backtrack(0, 0)
        return ret