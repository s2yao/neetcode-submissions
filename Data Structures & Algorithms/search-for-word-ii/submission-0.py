class Trie:
    def __init__(self):
        self.root = [None] * 27
        self.root[26] = False

    def put(self, word):
        curr_ptr = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not curr_ptr[idx]:
                curr_ptr[idx] = [None] * 27
                curr_ptr[idx][26] = False

            curr_ptr = curr_ptr[idx]

        curr_ptr[26] = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = set()
        visited = set()
        trie = Trie()

        def serialize(char):
            return ord(char) - ord('a')

        def dfs(row, col, ptr, progress):
            if (
                row < 0 or row >= len(board)
                or col < 0 or col >= len(board[0])
                or (row, col) in visited
            ):
                return

            idx = serialize(board[row][col])

            if not ptr[idx]:
                return

            # move trie pointer forward
            next_ptr = ptr[idx]
            progress += board[row][col]

            # current path forms a word
            if next_ptr[26]:
                ans.add(progress)

            visited.add((row, col))

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                dfs(row + dr, col + dc, next_ptr, progress)

            # backtrack
            visited.remove((row, col))

        for word in words:
            trie.put(word)

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie.root, "")

        return list(ans)