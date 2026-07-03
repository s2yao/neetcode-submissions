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

        stack = [(root, root.val)]
        ret = 0

        while stack:
            curr_node, curr_max = stack.pop()
            # decide if curr_node is good node
            if curr_node.val == curr_max:
                ret += 1

            if curr_node.left:
                if curr_node.left.val > curr_max:
                    stack.append((curr_node.left, curr_node.left.val))
                else:
                    stack.append((curr_node.left, curr_max))
            if curr_node.right:
                if curr_node.right.val > curr_max:
                    stack.append((curr_node.right, curr_node.right.val))
                else:
                    stack.append((curr_node.right, curr_max))
            
        return ret