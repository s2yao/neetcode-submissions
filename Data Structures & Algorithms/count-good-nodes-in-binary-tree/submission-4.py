# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = 0
        
        def tree_traversal(curr_node, curr_max):
            nonlocal ret
            if not curr_node:
                return

            if curr_node.val >= curr_max:
                curr_max = curr_node.val
                ret += 1

            tree_traversal(curr_node.left, curr_max)
            tree_traversal(curr_node.right, curr_max)


        tree_traversal(root, root.val)

        return ret