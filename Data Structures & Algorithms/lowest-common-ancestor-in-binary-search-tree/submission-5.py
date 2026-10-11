# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ret = None
        def traversal(curr_node) -> bool:
            nonlocal ret
            if not curr_node:
                return False

            left = traversal(curr_node.left)
            right = traversal(curr_node.right)

            curr_match = (curr_node == p) or (curr_node == q)
            
            if (left and right) or (curr_match and left) or (curr_match and right):
                ret = curr_node
            return left or right or curr_match
        
        traversal(root)
        return ret