class WordDictionary:

    def __init__(self):
        self.root = [None] * 27

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr[idx]:
                curr[idx] = [None] * 27
            curr = curr[idx]
        
        curr[26] = True

    def custom_search(self, word: str, curr: list):
        for char_idx in range(len(word)):
            if word[char_idx] == '.':
                for slot in range(len(curr) - 1):
                    if curr[slot]:
                        if self.custom_search(word[char_idx + 1:], curr[slot]):
                            return True
                # did not find
                return False
            else:
                char = word[char_idx]
                idx = ord(char) - ord('a')
                if not curr[idx]:
                    return False
                curr = curr[idx]
        return curr[26] == True

    def search(self, word: str) -> bool:
        return self.custom_search(word, self.root)

