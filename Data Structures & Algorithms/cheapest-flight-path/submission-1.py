class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dep = defaultdict(list)
        for start, end, cost in flights:
            dep[start].append([end, cost])

        min_heap = [[0, src, 0]] # cost, node, stops

        visited = set()
        
        while min_heap:
            curr_cost, curr_airport, stops = heapq.heappop(min_heap)
            if (curr_airport, stops) in visited:
                continue
            visited.add((curr_airport, stops))
            if curr_airport == dst:
                return curr_cost
            if stops > k:
                continue
            
            for next_airport, cost in dep[curr_airport]:
                if (next_airport, stops + 1) in visited:
                    continue
                heapq.heappush(min_heap, [cost + curr_cost, next_airport, stops + 1])

        return -1