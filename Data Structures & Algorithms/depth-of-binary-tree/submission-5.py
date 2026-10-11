# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        ret = 0
        while stack:
            curr_node, curr_depth = stack.pop()
            ret = max(ret, curr_depth)

            if curr_node.left:
                stack.append([curr_node.left, curr_depth + 1])
            if curr_node.right:
                stack.append([curr_node.right, curr_depth + 1])
        
        return ret