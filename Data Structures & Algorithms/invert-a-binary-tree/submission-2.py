# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root:
        #     left = self.invertTree(root.left)
        #     right = self.invertTree(root.right)
        #     root.right = left
        #     root.left = right
        # return root

        if not root:
            return None
        stack = [root]
        while stack:
            curr_node = stack.pop()
            left = curr_node.left
            right = curr_node.right
            curr_node.left = right
            curr_node.right = left

            if left:
                stack.append(left)
            if right:
                stack.append(right)

        return root