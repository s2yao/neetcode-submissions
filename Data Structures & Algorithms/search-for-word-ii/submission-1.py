class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def seedTrie(self, word):
        for each_word in word:
            curr_ptr = self.root
            for char in each_word:
                if char not in curr_ptr.children:
                    curr_ptr.children[char] = TrieNode()
                curr_ptr = curr_ptr.children[char]
            curr_ptr.end = True
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def check_bound_valid(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            return True
        
        self.seedTrie(words)

        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        curr_path = set()
        ret = []
        curr = []
        def dfs(row, col, curr_ptr):
            if (row, col) in curr_path:
                return
            curr_char = board[row][col]
            if curr_char not in curr_ptr.children:
                return
            curr.append(curr_char)
            curr_path.add((row, col))

            curr_ptr = curr_ptr.children[curr_char]
            if curr_ptr.end:
                ret.append("".join(curr))
                curr_ptr.end = False

            for dr, dc in direction:
                probe_row, probe_col = row + dr, col + dc
                if not check_bound_valid(probe_row, probe_col):
                    continue
                # print('hi')

                dfs(probe_row, probe_col, curr_ptr)
            curr_path.discard((row, col))
            curr.pop()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, self.root)

        return ret

