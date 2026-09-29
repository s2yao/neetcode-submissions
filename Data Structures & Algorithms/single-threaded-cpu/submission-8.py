class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = list(sorted([enqueue_time, process_time, idx] for idx, (enqueue_time, process_time) in enumerate(tasks)))

        curr_idx = 0
        curr_time = tasks[curr_idx][0]
        heap = []
        ret = []

        while curr_idx < len(tasks) and tasks[curr_idx][0] <= curr_time:
            heapq.heappush(heap, [tasks[curr_idx][1], tasks[curr_idx][2]])
            curr_idx += 1

        while heap:
            process_time, original_idx = heapq.heappop(heap)
            curr_time += process_time
            ret.append(original_idx)

            # if heap run out: update curr_time
            if not heap and curr_idx < len(tasks):
                curr_time = max(curr_time, tasks[curr_idx][0])

            # while add
            while curr_idx < len(tasks) and tasks[curr_idx][0] <= curr_time:
                heapq.heappush(heap, [tasks[curr_idx][1], tasks[curr_idx][2]])
                curr_idx += 1

        return ret