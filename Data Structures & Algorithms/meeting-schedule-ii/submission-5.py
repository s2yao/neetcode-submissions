class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        max_room = 0
        curr_room = 0

        start_arr = sorted(interval.start for interval in intervals)
        end_arr = sorted(interval.end for interval in intervals)
        start = 0
        end = 0

        while start < len(start_arr) and end < len(end_arr):
            if start_arr[start] >= end_arr[end]:
                curr_room -= 1
                end += 1
            
            curr_room += 1
            max_room = max(max_room, curr_room)
            start += 1
        
        return max_room