class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False
        
        dp = defaultdict(list)

        for node1, node2 in edges:
            dp[node1].append(node2)
            dp[node2].append(node1)
        
        visited = set()
        def dfs(curr_node):
            if curr_node in visited:
                return 
            
            visited.add(curr_node)

            for neighbor in dp[curr_node]:
                dfs(neighbor)
            
        dfs(0)
        return len(visited) == n