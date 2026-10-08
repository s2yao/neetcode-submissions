from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.dict_vals = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_vals[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_vals:
            return ""
        
        idx = bisect_right(self.dict_vals[key], timestamp, key = lambda x : x[0]) - 1
        if idx < 0:
            return ""

        return self.dict_vals[key][idx][1]