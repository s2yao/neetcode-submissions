class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row: int, col: int, idx: int) -> bool:
            # matched every character
            if idx == len(word):
                return True

            # out of bounds
            if row < 0 or row == rows or col < 0 or col == cols:
                return False

            # already used in current path
            if board[row][col] == "#":
                return False

            # current cell does not match needed character
            if board[row][col] != word[idx]:
                return False

            # mark current cell as visited
            original_char = board[row][col]
            board[row][col] = "#"

            # try all 4 directions
            found = (
                dfs(row - 1, col, idx + 1) or
                dfs(row + 1, col, idx + 1) or
                dfs(row, col - 1, idx + 1) or
                dfs(row, col + 1, idx + 1)
            )

            # backtrack
            board[row][col] = original_char

            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False