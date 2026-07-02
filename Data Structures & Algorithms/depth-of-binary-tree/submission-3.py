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
        # Bound a depth which each node
        ret = 1
        curr_depth = 1
        stack = [(root, curr_depth)]

        while stack:
            curr_node = stack.pop()
            curr_depth = curr_node[1]
            if not curr_node[0].left and not curr_node[0].right:
                ret = max(ret, curr_node[1])
            if curr_node[0].left:
                stack.append((curr_node[0].left, curr_depth + 1))
            if curr_node[0].right:
                stack.append((curr_node[0].right, curr_depth + 1))
        
        return ret