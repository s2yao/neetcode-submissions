class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, curr_root): 
        while curr_root != self.parent[curr_root]:
            # update
            self.parent[curr_root] = self.parent[self.parent[curr_root]]
            # move to next
            curr_root = self.parent[curr_root]
        return curr_root

    def union(self, node1, node2): 
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2: # common root
            return False
        
        # merge to the bigger
        if self.size[root2] > self.size[root1]:
            root2, root1 = root1, root2
        
        # update parent
        self.parent[root2] = root1
        # update size
        self.size[root1] += self.size[root2]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        ret = n
        # construct unionfind
        for node1, node2 in edges:
            if uf.union(node1, node2):
                ret -= 1
        
        return ret

# n = 2, edges = [[0,1],[1,2],[3,4],[0,2]]
# self.parent = [0, 0, 0, 3, 3]
# self.size = [3, 1, 1, 2, 1]
# node1, node2 = 02
# root1, root2 = 00