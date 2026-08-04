# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root: 
        #     return
        
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)

        # root.left = right
        # root.right = left

        # return root
        if not root:
            return root
        process = [root]

        while process:
            curr_node = process.pop()
            if curr_node.left:
                process.append(curr_node.left)
            if curr_node.right:
                process.append(curr_node.right)
            
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
        
        return root