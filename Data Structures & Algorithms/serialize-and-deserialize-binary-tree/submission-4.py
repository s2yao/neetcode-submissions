# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
            
        def create_node(val):
            if val == "#":
                return None
            return TreeNode(int(val))

        # global curr_idx
        self.curr_idx = 0

        # function that recursively take one subtree
        # catching left and right
        def create_tree(root):
            self.curr_idx += 1
            if not root:
                return None
            
            left_node = create_tree(create_node(data[self.curr_idx]))
            right_node = create_tree(create_node(data[self.curr_idx]))
            
            root.left = left_node
            root.right = right_node
            
            return root

        # make root and
        # call function
        return create_tree(create_node(data[self.curr_idx]))

