class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks.sort()
        new_tasks = list(sorted([task_enqueue_time, task_process_time, idx] for idx, (task_enqueue_time, task_process_time) in enumerate(tasks)))
        print(new_tasks)
        
        min_heap = []
        heapq.heappush(min_heap, [new_tasks[0][1], new_tasks[0][2]])
        curr_idx = 1
        curr_time = new_tasks[0][0]
        ret = []
        
        while curr_idx < len(new_tasks) or min_heap:
            if not min_heap:
                curr_time = max(curr_time, new_tasks[curr_idx][0])

            while curr_idx < len(new_tasks) and new_tasks[curr_idx][0] <= curr_time:
                enqueue_time, process_time, original_idx = new_tasks[curr_idx]
                heapq.heappush(min_heap, [process_time, original_idx])
                curr_idx += 1

            process_time, original_idx = heapq.heappop(min_heap)
            curr_time += process_time
            ret.append(original_idx)
        
        return ret