"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbor = None):
        self.val = val
        self.neighbors = neighbor if neighbor else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_idx = [None] * 101
        node_idx[node.val] = Node(node.val)

        process = [node]
        visited = set()

        while process:
            curr_node = process.pop()

            if curr_node in visited:
                continue
            visited.add(curr_node)

            copy_node = node_idx[curr_node.val]

            for neighbor in curr_node.neighbors:
                if node_idx[neighbor.val] is None:
                    node_idx[neighbor.val] = Node(neighbor.val)

                copy_node.neighbors.append(node_idx[neighbor.val])

                if neighbor not in visited:
                    process.append(neighbor)

        return node_idx[node.val]