class Solution:
    def solve(self, board: List[List[str]]) -> None:
        all_posn = set()
        edge_land = []

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    if row == 0 or col == 0 or col == len(board[0]) - 1 or row == len(board) - 1:
                        edge_land.append((row, col))
                    else:
                        all_posn.add((row, col))
        
        def check(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if board[row][col] != "O":
                return False
            return True

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        while edge_land:
            row, col = edge_land.pop()
            
            for dr, dc in directions:
                probe_row, probe_col = dr + row, dc + col
                if not check(probe_row, probe_col) or (probe_row, probe_col) in visited:
                    continue
                visited.add((probe_row, probe_col))
                all_posn.discard((probe_row, probe_col))
                edge_land.append((probe_row, probe_col))
        
        for clear_row, clear_col in all_posn:
            board[clear_row][clear_col] = "X"