class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0

        def build(inorder_part):
            if not inorder_part:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_part.index(root_val)

            left_inorder = inorder_part[:mid]
            right_inorder = inorder_part[mid + 1:]

            root.left = build(left_inorder)
            root.right = build(right_inorder)

            return root

        return build(inorder)