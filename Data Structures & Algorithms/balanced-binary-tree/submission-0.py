# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        def in_order(root):
            if not root:
                return 0
            left = 0
            right = 0
            
            if root.left:
                left = in_order(root.left)
            if root.right:
                right = in_order(root.right)
            
            if abs(left - right) > 1:
                self.ret = False
            
            return 1 + max(left, right)

        in_order(root)
        return self.ret