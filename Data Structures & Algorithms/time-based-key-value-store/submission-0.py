from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr_val_time = self.key_val[key]

        # binary search
        left = 0
        right = len(arr_val_time) - 1
        ret = ""

        while left <= right:
            mid = (left + right) // 2
            if arr_val_time[mid][1] <= timestamp:
                ret = arr_val_time[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return ret


