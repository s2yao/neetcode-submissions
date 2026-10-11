from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = defaultdict(int)

        for idx, val in enumerate(inorder):
            inorder_map[val] = idx

        preorder_idx = 0

        def dfs(left, right):
            nonlocal preorder_idx

            if left > right:
                return None

            # Get the current root from preorder
            root_val = preorder[preorder_idx]
            preorder_idx += 1

            root = TreeNode(root_val)

            # Find the root position in inorder
            split_idx = inorder_map[root_val]

            # Build left and right subtrees
            root.left = dfs(left, split_idx - 1)
            root.right = dfs(split_idx + 1, right)

            return root

        return dfs(0, len(inorder) - 1)