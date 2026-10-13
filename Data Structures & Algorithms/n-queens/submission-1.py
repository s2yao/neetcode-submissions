class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        pos_dia = set()
        negative_dia = set()

        def row_col_convert(num):
            return [num // n, num % n]
        
        def output_convert(col):
            row = []
            for c in range(n):
                if col == c:
                    row.append("Q")
                else:
                    row.append(".")
            return ''.join(row)

        curr = []
        ret = []
        def backtrack(idx, queen_left):
            if queen_left == 0:
                ret.append(curr.copy())
                return
            if idx == n * n:
                return
            
            for i in range(idx, idx + n):
                curr_row, curr_col = row_col_convert(i)
                if curr_col in col_set or (curr_row - curr_col) in negative_dia or (curr_row + curr_col) in pos_dia:
                    continue
                negative_dia.add((curr_row - curr_col))
                pos_dia.add((curr_row + curr_col))
                col_set.add(curr_col)
                curr.append(output_convert(curr_col))
                backtrack(idx + n, queen_left - 1)
                curr.pop()
                negative_dia.discard((curr_row - curr_col))
                pos_dia.discard((curr_row + curr_col))
                col_set.discard(curr_col)
        
        backtrack(0, n)
        return ret