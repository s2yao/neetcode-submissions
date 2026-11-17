class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        curr_node_idx = 0
        ret = 0
        all_dis = defaultdict(lambda: float('inf'))
        all_dis[0] = 0

        for _ in range(len(points)):
            visited.add(curr_node_idx)
            fuck = None
            for i in range(len(points)):
                if i in visited:
                    continue
                curr_node_x, curr_node_y = points[curr_node_idx]
                probe_node_x, probe_node_y = points[i]
                curr_distance = abs(curr_node_x - probe_node_x) + abs(curr_node_y - probe_node_y)
                all_dis[i] = min(all_dis[i], curr_distance)
                if not fuck or all_dis[i] < all_dis[fuck]:
                    fuck = i

            ret += all_dis[curr_node_idx]
            curr_node_idx = fuck
        
        return ret