class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        count = Counter(tasks)
        # find the most occur count
        max_occ = max(count.values())

        # find the number of char with most occur count
        max_chars = 0
        for value in count.values():
            if value == max_occ:
                max_chars += 1

        return max(len(tasks), max_chars + (n + 1) * (max_occ - 1))
