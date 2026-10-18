class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dep = defaultdict(list)

        for node1, node2, weight in times:
            dep[node1].append([node2, weight])

        ret = 0

        min_heap = [[0, k]]
        visited = set()

        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            ret = curr_weight

            for neighbor, weight in dep[curr_node]:
                heapq.heappush(min_heap, [curr_weight + weight, neighbor])
        
        if len(visited) != n:
            return -1
        return ret