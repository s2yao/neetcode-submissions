class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for y in range(9):
            seen = set()
            for x in range(9):
                v = board[y][x]
                if v == ".": 
                    continue
                if v in seen:
                    return False
                seen.add(v)

        # cols
        for x in range(9):
            seen = set()
            for y in range(9):
                v = board[y][x]
                if v == ".": 
                    continue
                if v in seen:
                    return False
                seen.add(v)

        # 3x3 boxes
        for box_y in range(0, 9, 3):
            for box_x in range(0, 9, 3):
                seen = set()
                for i in range(box_y, box_y + 3):
                    for j in range(box_x, box_x + 3):
                        v = board[i][j]
                        if v == ".":
                            continue
                        if v in seen:
                            return False
                        seen.add(v)

        return True
