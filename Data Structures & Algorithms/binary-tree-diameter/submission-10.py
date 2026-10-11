# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [[root, False]]
        dict_depth = defaultdict(int)
        ret = 0
        while stack:
            curr_node, visited = stack.pop()

            if not curr_node:
                continue
            
            if not visited:
                stack.append([curr_node, True])
                stack.append([curr_node.right, False])
                stack.append([curr_node.left, False])
            else:
                left_depth = dict_depth[curr_node.left]
                right_depth = dict_depth[curr_node.right]
                curr_depth = left_depth + right_depth
                ret = max(ret, curr_depth)
                dict_depth[curr_node] = max(left_depth, right_depth) + 1

        return ret