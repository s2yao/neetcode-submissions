class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        # Initialize both search frontiers
        begin_set = {beginWord}
        end_set = {endWord}
        word_set.discard(beginWord)
        word_set.discard(endWord)

        steps = 1

        while begin_set and end_set:
            # Always expand the smaller frontier
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()

            for curr_word in begin_set:
                for i in range(len(curr_word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = curr_word[:i] + char + curr_word[i + 1:]

                        # Both searches have connected
                        if new_word in end_set:
                            return steps + 1

                        if new_word not in word_set:
                            continue

                        # Mark as visited immediately
                        word_set.remove(new_word)
                        next_set.add(new_word)

            begin_set = next_set
            steps += 1

        return 0