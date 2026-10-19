class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        curr_stop = 0
        init_cost = 0
        min_heap = [[init_cost, src, curr_stop]]

        dep = defaultdict(list)
        for start, end, cost in flights:
            dep[start].append([end, cost])

        ret = 0
        visited = set() # airport, and their current k

        while min_heap:
            curr_cost, curr_airport, curr_stops = heapq.heappop(min_heap)
            if curr_airport == dst:
                return curr_cost
            if curr_stops > k:
                continue
            if (curr_airport, curr_stops) in visited:
                continue
            visited.add((curr_airport, curr_stops))

            for next_airport, cost in dep[curr_airport]:
                if (next_airport, curr_stops + 1) in visited:
                    continue
                # print(curr_cost)
                heapq.heappush(min_heap, (curr_cost + cost, next_airport, curr_stops + 1))
        
        return -1