# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
                k -= 1
                if k == 0:
                    return curr_node.val

        return -1