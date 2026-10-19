class TrieNode:
    def __init__ (self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_ptr = self.root

        for char in word:
            if char not in curr_ptr.children:
                curr_ptr.children[char] = TrieNode()
            curr_ptr = curr_ptr.children[char]
        curr_ptr.end = True


    def search(self, word: str) -> bool:

        def search_word(idx, curr_ptr):
            if idx == len(word):
                return curr_ptr.end
            
            for i in range(idx, len(word)):
                curr_char = word[i]
                if curr_char == '.':
                    for char in curr_ptr.children:
                        if search_word(idx + 1, curr_ptr.children[char]):
                            return True
                    return False
                else:
                    if curr_char not in curr_ptr.children:
                        return False
                    else:
                        return search_word(idx + 1, curr_ptr.children[curr_char])

        return search_word(0, self.root)
