# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0

        def traversal(root, curr_max):
            nonlocal ret
            if not root:
                return

            next_max = curr_max
            if curr_max <= root.val:
                ret += 1
                next_max = root.val
            
            traversal(root.left, next_max)
            traversal(root.right, next_max)
        traversal(root, root.val)
        return ret
            