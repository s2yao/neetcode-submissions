class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # number of cycle == most_freq
        # Last cycle == number of most_freq
        # every cycle length == len(n) + 1
        
        freq_dict = defaultdict(int)
        max_freq = 0
        for ele in tasks:
            freq_dict[ele] += 1
            max_freq = max(max_freq, freq_dict[ele])
        
        chars_of_max_freq = 0
        for freq in freq_dict.values():
            if freq == max_freq:
                chars_of_max_freq += 1

        ret = (max_freq - 1) * (n + 1) + chars_of_max_freq
        return max(ret, len(tasks))