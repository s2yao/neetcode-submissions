# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def traversal(root, depth):
            nonlocal ret
            if not root:
                return
            ret = max(depth, ret)
            if root.left:
                traversal(root.left, depth + 1)
            if root.right:
                traversal(root.right, depth + 1)
        
        traversal(root, 1)
        return ret