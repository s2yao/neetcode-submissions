# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def inorder(curr_node):
            nonlocal prev
            if not curr_node:
                return True
            
            if not inorder(curr_node.left):
                return False
            if curr_node.val <= prev:
                return False
            prev = curr_node.val
            if not inorder(curr_node.right):
                return False
            return True
        
        return inorder(root)
    
    # prev = -inf
    # prev = 2