# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ret = True
        def dfs(node1, node2):
            Valid = (node1 and node2)
            if not Valid:
                if not node1 and not node2:
                    return
                else:
                    self.ret = False
                    return
            if node1.val != node2.val:
                self.ret = False
            next_node1 = None
            next_node2 = None

            # left
            if node1:
                next_node1 = node1.left
            if node2:
                next_node2 = node2.left
            
            dfs(next_node1, next_node2)

            # right
            if node1:
                next_node1 = node1.right
            if node2:
                next_node2 = node2.right
            
            dfs(next_node1, next_node2)
        
        dfs(p, q)

        return self.ret