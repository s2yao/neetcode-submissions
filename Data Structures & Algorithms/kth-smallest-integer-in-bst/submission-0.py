# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        # seed everything into preorder array
        self.preorder = []

        def preorder_append(root):
            if not root:
                return
            
            if root.left:
                preorder_append(root.left)
            self.preorder.append(root)
            if root.right:
                preorder_append(root.right)
        
        preorder_append(root)
        return self.preorder[k-1].val