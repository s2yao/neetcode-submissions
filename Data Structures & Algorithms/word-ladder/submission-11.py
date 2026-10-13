class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([beginWord])
        visited = {beginWord}
        steps = 1

        while queue:
            level_len = len(queue)

            for _ in range(level_len):
                curr_word = queue.popleft()

                if curr_word == endWord:
                    return steps

                # Try replacing every character
                for i in range(len(curr_word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = curr_word[:i] + char + curr_word[i + 1:]

                        if new_word not in word_set:
                            continue

                        if new_word in visited:
                            continue

                        visited.add(new_word)
                        queue.append(new_word)

            steps += 1

        return 0