class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        start_ptr = 0
        end_ptr = 0

        rooms = 0
        max_rooms = 0

        while start_ptr < len(intervals):
            if starts[start_ptr] >= ends[end_ptr]:
                rooms -= 1
                end_ptr += 1

            rooms += 1
            max_rooms = max(max_rooms, rooms)
            start_ptr += 1

        return max_rooms
        