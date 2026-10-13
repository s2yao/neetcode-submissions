class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        def find(curr_word):
            avail = []
            for word in wordList:
                if word in visited:
                    continue
                i = 0
                diff = 0
                for i in range(len(word)):
                    if word[i] != curr_word[i]:
                        diff += 1
                if diff == 1:
                    avail.append(word)
            return avail

        queue = deque()
        queue.extend(find(beginWord))
        ret = 0
        while queue:
            curr_len = len(queue)
            ret += 1

            for _ in range(curr_len):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return ret + 1
                visited.add(curr_word)

                queue.extend(find(curr_word))
        
        return 0