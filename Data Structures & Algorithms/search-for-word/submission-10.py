class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check_bound(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            return True
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_path = set()
        def backtrack(row, col, word_idx):
            curr_letter = word[word_idx]
            if (row, col) in curr_path:
                return False
            if curr_letter != board[row][col]:
                return False
            word_idx += 1
            if word_idx == len(word):
                return True
            curr_path.add((row, col))
            for dr, dc in directions:
                probe_row, probe_col = row + dr, col + dc
                if not check_bound(probe_row, probe_col):
                    continue
                if backtrack(probe_row, probe_col, word_idx):
                    return True
            
            curr_path.discard((row, col))
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        
        return False