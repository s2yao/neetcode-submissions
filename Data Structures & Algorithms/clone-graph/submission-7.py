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

        clones = {node: Node(node.val)}
        process = [node]

        while process:
            curr = process.pop()

            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    process.append(neighbor)

                clones[curr].neighbors.append(clones[neighbor])

        return clones[node]