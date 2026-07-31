class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        def backtrack(i, trie, memo):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            cur = trie.root
            j = i
            while j < len(s):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.word_end:
                    if backtrack(j + 1, trie, memo):
                        return True
                j += 1
            memo[i] = False
            return False

        return backtrack(0, trie, {})

        