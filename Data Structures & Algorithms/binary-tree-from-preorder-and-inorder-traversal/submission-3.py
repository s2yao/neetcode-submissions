class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_idx = 0

        def merge(inorder):
            if not inorder:
                return None

            curr_root = preorder[self.preorder_idx]
            self.preorder_idx += 1

            # find exact index
            split_idx = inorder.index(curr_root)

            left = merge(inorder[:split_idx])
            right = merge(inorder[split_idx + 1:])

            new_node = TreeNode(curr_root)

            new_node.left = left
            new_node.right = right

            return new_node
        
        return merge(inorder)