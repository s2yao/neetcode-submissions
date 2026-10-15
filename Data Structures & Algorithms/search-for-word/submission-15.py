class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 1 and len(board[0]) == 1 and len(word) == 1 and word == board[0][0]:
            return True
        curr_path = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def backtrack(row, col, curr_str_idx):
            if curr_str_idx == len(word):
                return True
            target_letter = word[curr_str_idx]
            curr_letter = board[row][col]
            # print(row, col, curr_letter, target_letter)
            # print(curr_path)
            if target_letter != curr_letter:
                return False
            if (row, col) in curr_path:
                return False
            curr_path.add((row, col))
            for dr, dc in directions:
                if row + dr < 0 or col + dc < 0 or row + dr >= len(board) or col + dc >= len(board[0]):
                    continue
                if backtrack(row + dr, col + dc, curr_str_idx + 1):
                    return True
            curr_path.discard((row, col))
            # all 4 dir rejected, reject curr
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        return False

["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]