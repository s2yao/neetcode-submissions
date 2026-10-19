class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_ptr = self.root

        for char in word:
            if char not in curr_ptr.children:
                curr_ptr.children[char] = TrieNode()
            curr_ptr = curr_ptr.children[char]
        curr_ptr.end = True

    def search(self, word: str) -> bool:
        curr_ptr = self.root

        for char in word:
            if char not in curr_ptr.children:
                return False
            curr_ptr = curr_ptr.children[char]
        
        return curr_ptr.end

    def startsWith(self, prefix: str) -> bool:
        curr_ptr = self.root

        for char in prefix:
            if char not in curr_ptr.children:
                return False
            curr_ptr = curr_ptr.children[char]
        
        return True
        
        