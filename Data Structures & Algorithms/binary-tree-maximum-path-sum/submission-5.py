# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = root.val
        
        def post_traversal(curr_node) -> int:
            nonlocal ret
            if not curr_node:
                return 0

            left = max(0, post_traversal(curr_node.left))
            right = max(0, post_traversal(curr_node.right))
            
            curr_sum = curr_node.val + left + right
            ret = max(ret, curr_sum)

            return max(left + curr_node.val, right + curr_node.val)

        post_traversal(root)
        return ret