class Solution:
    def checkValidString(self, s: str) -> bool:
        balance = 0

        # 把 * 当成 (
        for char in s:
            if char == ")":
                balance -= 1
            else:  # ( or *
                balance += 1

            if balance < 0:
                return False

        balance = 0

        # 把 * 当成 )
        for char in reversed(s):
            if char == "(":
                balance -= 1
            else:  # ) or *
                balance += 1

            if balance < 0:
                return False

        return True