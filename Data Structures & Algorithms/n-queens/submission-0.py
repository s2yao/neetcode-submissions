class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []

        board = []
        for _ in range(n):
            board.append(["."] * n)

        used_cols = set()
        used_pos_diag = set()  # row + col
        used_neg_diag = set()  # row - col

        def dfs(row):
            if row == n:
                curr_board = []

                for r in range(n):
                    curr_board.append("".join(board[r]))

                ret.append(curr_board)
                return

            for col in range(n):
                pos_diag = row + col
                neg_diag = row - col

                if col in used_cols:
                    continue

                if pos_diag in used_pos_diag:
                    continue

                if neg_diag in used_neg_diag:
                    continue

                board[row][col] = "Q"
                used_cols.add(col)
                used_pos_diag.add(pos_diag)
                used_neg_diag.add(neg_diag)

                dfs(row + 1)

                board[row][col] = "."
                used_cols.remove(col)
                used_pos_diag.remove(pos_diag)
                used_neg_diag.remove(neg_diag)

        dfs(0)
        return ret