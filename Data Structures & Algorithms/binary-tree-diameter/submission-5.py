# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ret = 0

        def dfs(root):
            if not root:
                return 0
            left_val, right_val = 0, 0
            
            if root.left:
                left_val = dfs(root.left)
            if root.right:
                right_val = dfs(root.right)
            
            self.ret = max(self.ret, left_val + right_val)

            return 1 + max(left_val, right_val)
        
        dfs(root)

        return self.ret