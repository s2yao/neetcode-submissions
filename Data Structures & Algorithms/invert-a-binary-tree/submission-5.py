# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [[root, False]]

        while stack:
            curr_node, visited = stack.pop()

            if not curr_node:
                continue

            if not visited:
                stack.append([curr_node.right, False])
                stack.append([curr_node.left, False])
                stack.append([curr_node, True])
            else:
                curr_node.left, curr_node.right = curr_node.right, curr_node.left
        
        return root
