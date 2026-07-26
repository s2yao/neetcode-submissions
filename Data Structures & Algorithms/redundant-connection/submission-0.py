class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def find(self, curr_node):
        while curr_node != self.parent[curr_node]:
            # update
            self.parent[curr_node] = self.parent[self.parent[curr_node]]
            # next
            curr_node = self.parent[curr_node]
        return curr_node

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False # this returns when current 2 nodes creates a cycle

        # add to bigger set
        if self.size[root2] < self.size[root1]:
            root2, root1 = root1, root2
        
        # update parent
        self.parent[root2] = root1
        # update size
        self.size[root1] += self.size[root2]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ret = []
        uf = UnionFind(len(edges))
        # iteration through all edges return latest
        for node1, node2 in edges:
            if not uf.union(node1 - 1, node2 - 1):
                ret = [node1, node2]
        
        return ret