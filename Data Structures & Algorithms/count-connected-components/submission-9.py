class UnionFind:
    def __init__ (self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1] * size
    
    def find(self, curr_val):
        while curr_val != self.parents[curr_val]:
            self.parents[curr_val] = self.parents[self.parents[curr_val]]
            curr_val = self.parents[curr_val]
        return curr_val
    
    def union_find(self, val1, val2):
        root1 = self.find(val1)
        root2 = self.find(val2)

        if root1 == root2:
            return 0
        
        if root1 < root2:
            root1, root2 = root2, root1
        
        self.parents[root2] = root1
        self.sizes[root1] += self.sizes[root2]
        return 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        ret = n
        for start, end in edges:
            ret -= uf.union_find(start, end)
        
        return ret