# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.best_root = root
        def dfs(root):
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            # if curr node is target
            curr = (root.val == p.val or root.val == q.val)

            # if curr node is target & left or right contains target
            # if left and right both contains target
            if (curr and (left or right)) or (left and right):
                self.best_root = root

            return (left or right or curr)
        dfs(root)
        return self.best_root