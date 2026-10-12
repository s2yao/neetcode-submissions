class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def find(self, curr_node):
        while curr_node != self.parent[curr_node]:
            self.parent[curr_node] = self.parent[self.parent[curr_node]]
            curr_node = self.parent[curr_node]
        
        return curr_node
    
    def union(self, val1, val2):
        root1 = self.find(val1)
        root2 = self.find(val2)

        if root1 == root2:
            return False
        
        if root1 < root2:
            root1, root2 = root2, root1
        
        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False
        dsu = DSU(n)
        for node1, node2 in edges:
            if not dsu.union(node1, node2): 
                return False
        
        return True
            