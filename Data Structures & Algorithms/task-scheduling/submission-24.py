class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        max_freq = max(count.values())
        max_freq_chars = 0
        
        for char, freq in count.items():
            if freq == max_freq:
                max_freq_chars += 1
        
        lower_bound = (n + 1) * (max_freq - 1) + max_freq_chars
        upper_bound = len(tasks)
        return max(lower_bound, upper_bound)