class dsu:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def find(self, curr_val):
        while curr_val != self.parent[curr_val]:
            self.parent[curr_val] = self.parent[self.parent[curr_val]]
            curr_val = self.parent[curr_val]
        return curr_val
    
    def union(self, val1, val2):
        root1 = self.find(val1)
        root2 = self.find(val2)

        if root1 == root2:
            return False
        
        if self.size[root1] < self.size[root2]:
            root1, root2 = root2, root1
        
        self.parent[root2] = root1
        self.size[root1] += root2
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nigger = dsu(n)
        ret = n
        for node1, node2 in edges:
            if nigger.union(node1, node2):
                ret -= 1
        
        return ret