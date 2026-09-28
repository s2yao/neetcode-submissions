class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((start, time, i) for i, (start, time) in enumerate(tasks))

        heap = []
        ret = []
        i = 0
        curr_time = tasks[0][0]

        # add all tasks available at the first arrival time
        while i < len(tasks) and tasks[i][0] <= curr_time:
            start, time, idx = tasks[i]
            heapq.heappush(heap, (time, idx))
            i += 1

        while heap:
            time, idx = heapq.heappop(heap)
            curr_time += time
            ret.append(idx)

            # CPU idle -> jump to next task
            if not heap and i < len(tasks) and tasks[i][0] > curr_time:
                curr_time = tasks[i][0]

            # add everything that has arrived
            while i < len(tasks) and tasks[i][0] <= curr_time:
                start, time, idx = tasks[i]
                heapq.heappush(heap, (time, idx))
                i += 1

        return ret