class PrefixTree:

    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        ptr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not ptr[idx]:
                ptr[idx] = [None] * 27
            ptr = ptr[idx]
        
        ptr[26] = True


    def search(self, word: str) -> bool:
        ptr = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if ptr[idx] is None:
                return False

            ptr = ptr[idx]

        return ptr[26] == True
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root

        for char in prefix:
            idx = ord(char) - ord('a')

            if ptr[idx] is None:
                return False

            ptr = ptr[idx]

        return True