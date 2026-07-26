class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, curr_node):
        while curr_node != self.parent[curr_node]:
            self.parent[curr_node] = self.parent[self.parent[curr_node]]
            curr_node = self.parent[curr_node]
        return curr_node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False # cycle detected
        
        # bigger set gets append
        if self.size[root1] < self.size[root2]:
            root2, root1 = root1, root2
        
        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # see if connected
            return False
            
        uf = UnionFind(n)
        for node1, node2 in edges:
            if not uf.union(node1, node2):
                return False
        
        return True