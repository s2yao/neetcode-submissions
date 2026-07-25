class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board)

        def check(row, col, idx):
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1:
                return False
            curr_ele = board[row][col]
            return curr_ele != "#" and curr_ele == word[idx]

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            
            # check valid
            # same string as word[idx]
            # if current posn == "#"
            if not check(row, col, idx):
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            result = dfs(row + 1, col, idx + 1) or \
                    dfs(row - 1, col, idx + 1) or \
                    dfs(row, col + 1, idx + 1) or \
                    dfs(row, col - 1, idx + 1)
            board[row][col] = temp

            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        
        return False
        