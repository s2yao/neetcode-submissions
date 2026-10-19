# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_idx = 0
        idx_map = defaultdict(int)
        for idx, ele in enumerate(inorder):
            idx_map[ele] = idx

        def merge(left, right):
            if left > right:
                return None
            curr_root = preorder[self.preorder_idx]
            self.preorder_idx += 1
            curr_idx = idx_map[curr_root]
            
            left = merge(left, curr_idx - 1)
            right = merge(curr_idx + 1, right)

            new_node = TreeNode(curr_root)
            new_node.left = left
            new_node.right = right

            return new_node
        return merge(0, len(preorder) - 1)