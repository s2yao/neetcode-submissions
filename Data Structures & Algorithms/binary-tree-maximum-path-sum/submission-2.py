# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val

        def post_order(root):
            if not root:
                return 0

            left_val = 0
            right_val = 0

            if root.left:
                left_val = post_order(root.left)
            if root.right:
                right_val = post_order(root.right)

            curr_stack_max = (root.val + max(left_val, 0) + max(right_val, 0))
            self.ans = max(self.ans, curr_stack_max)
            
            return root.val + max(max(left_val, 0), max(right_val, 0))
        
        post_order(root)
        return self.ans

