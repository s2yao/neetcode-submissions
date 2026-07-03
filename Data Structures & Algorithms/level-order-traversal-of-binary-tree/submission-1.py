# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        if not root:
            return ret

        stack = [root]

        while True:
            if not stack:
                break
            ret.append([node.val for node in stack])
            next_level = []
            for curr_node in stack:
                if curr_node.left:
                    next_level.append(curr_node.left)
                if curr_node.right:
                    next_level.append(curr_node.right)
            stack = next_level
        
        return ret