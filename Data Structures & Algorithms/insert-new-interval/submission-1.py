class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []

        # Find the insertion index based on interval start.
        def binary_search(target: int) -> int:
            left = 0
            right = len(intervals)

            while left < right:
                mid = (left + right) // 2

                if intervals[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        # Merge newInterval with all overlapping intervals.
        def merge_interval(idx: int) -> int:
            ret_start, ret_end = newInterval

            while (
                idx < len(intervals)
                and intervals[idx][0] <= ret_end
            ):
                ret_start = min(ret_start, intervals[idx][0])
                ret_end = max(ret_end, intervals[idx][1])
                idx += 1

            ret.append([ret_start, ret_end])
            return idx

        found_idx = binary_search(newInterval[0])

        # The interval immediately before the insertion position
        # may also overlap with newInterval.
        if (
            found_idx > 0
            and intervals[found_idx - 1][1] >= newInterval[0]
        ):
            found_idx -= 1

        for i in range(found_idx):
            ret.append(intervals[i])

        merge_up_to = merge_interval(found_idx)

        for i in range(merge_up_to, len(intervals)):
            ret.append(intervals[i])

        return ret