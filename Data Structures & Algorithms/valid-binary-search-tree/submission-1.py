# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")
        stack = [[root, False]]

        while stack:
            curr_node, visited = stack.pop()

            if not curr_node:
                continue
            
            if not visited:
                stack.append([curr_node.right, False])
                stack.append([curr_node, True])
                stack.append([curr_node.left, False])
            else:
                if prev >= curr_node.val:
                    return False
                prev = curr_node.val
            
        return True