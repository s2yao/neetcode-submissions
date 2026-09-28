class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((start, time, i) for i, (start, time) in enumerate(tasks))

        heap = []
        ret = []
        i = 0
        curr_time = 0

        while i < len(tasks) or heap:
            if not heap:
                curr_time = max(curr_time, tasks[i][0])

            while i < len(tasks) and tasks[i][0] <= curr_time:
                start, time, idx = tasks[i]
                heapq.heappush(heap, (time, idx))
                i += 1

            time, idx = heapq.heappop(heap)
            curr_time += time
            ret.append(idx)

        return ret