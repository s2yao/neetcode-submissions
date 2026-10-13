class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        pos_dia = set()
        negative_dia = set()
        
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
        def backtrack(row):
            if row == n:
                ret.append(curr.copy())
                return
            
            for col in range(n):
                if col in col_set or (row + col) in pos_dia or (row - col) in negative_dia:
                    continue
                
                col_set.add(col)
                pos_dia.add((row + col))
                negative_dia.add((row - col))
                curr.append(output_convert(col))
                backtrack(row + 1)
                curr.pop()
                col_set.discard(col)
                pos_dia.discard((row + col))
                negative_dia.discard((row - col))

        backtrack(0)
        return ret