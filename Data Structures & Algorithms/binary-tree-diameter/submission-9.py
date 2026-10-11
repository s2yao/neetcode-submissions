# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def traversal(root) -> int:
            nonlocal ret
            if not root:
                return 0
            
            left = traversal(root.left)
            right = traversal(root.right)

            curr_dia = left + right
            ret = max(ret, curr_dia)

            return max(left, right) + 1
        
        traversal(root)
        return ret