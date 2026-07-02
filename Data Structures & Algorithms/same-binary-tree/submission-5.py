# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif q and p and q.val == p.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        else:
            return False