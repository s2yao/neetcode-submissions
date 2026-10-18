"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by start
        start = [val.start for val in sorted(intervals, key = lambda x: x.start)]
        # sort by end
        end = [val.end for val in sorted(intervals, key = lambda x: x.end)]
        idx_start = idx_end = 0

        max_overlap = 0
        curr_overlap = 0
        # iteration through all the start
        while idx_start < len(intervals) and idx_end < len(intervals):
            # if start time > end: overlap -= 1
            if start[idx_start] < end[idx_end]:
                curr_overlap += 1
                idx_start += 1
            # if start time <= end: overlap += 1
            else:
                curr_overlap -= 1
                idx_end += 1
            
            # max_overlap update
            max_overlap = max(max_overlap, curr_overlap)

        return max_overlap