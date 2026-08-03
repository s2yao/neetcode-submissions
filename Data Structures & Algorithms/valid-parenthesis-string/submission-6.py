class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # 最少可能剩下多少个未匹配的 (
        high = 0  # 最多可能剩下多少个未匹配的 (

        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            else:  # *
                low -= 1      # 把 * 当成 )
                high += 1     # 把 * 当成 (

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0