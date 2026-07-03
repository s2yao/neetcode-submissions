# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # layer to layer
        if not root:
            return []

        stack = [root]
        ret = []

        while stack:
            next_level = []
            right_most = stack[-1] # right most as last ele?
            ret.append(right_most.val)
            for node in stack:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack = next_level

        return ret