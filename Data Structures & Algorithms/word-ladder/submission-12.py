from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = defaultdict(list)

        # Build wildcard patterns for every word
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                word_dict[pattern].append(word)

        # Find all neighbors differing by one character
        def find(curr_word):
            avail = []

            for i in range(len(curr_word)):
                pattern = curr_word[:i] + "*" + curr_word[i + 1:]

                avail.extend(word_dict[pattern])

                # Avoid processing the same pattern again
                # word_dict[pattern].clear()

            return avail

        # BFS: explore shortest transformations first
        queue = deque([beginWord])
        visited = {beginWord}
        steps = 1

        while queue:
            level_len = len(queue)

            for _ in range(level_len):
                curr_word = queue.popleft()

                if curr_word == endWord:
                    return steps

                for next_word in find(curr_word):
                    if next_word in visited:
                        continue

                    visited.add(next_word)
                    queue.append(next_word)

            steps += 1

        return 0