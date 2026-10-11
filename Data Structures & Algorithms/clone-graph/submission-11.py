"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        dict_map_and_visit = {node: Node(node.val)}
        
        while stack:
            curr_node = stack.pop()

            for neighbor in curr_node.neighbors:
                if neighbor not in dict_map_and_visit:
                    dict_map_and_visit[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                dict_map_and_visit[curr_node].neighbors.append(dict_map_and_visit[neighbor])
        
        return dict_map_and_visit[node]
