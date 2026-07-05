# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # preorder
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        data = data.split(',')

        def create_node(val):
            if val == "#":
                return None
            else:
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

















    #     if not data:
    #         return None

    #     def create_node(char: str):
    #         if char == "#":
    #             return None
    #         else:
    #             return TreeNode(int(char))
                
    #     # queue to store nodes await process
    #     queue = deque()
    #     root = create_node(data[0])
    #     queue.append(root)
    #     idx = 0
        
    #     # construct tree from nodes await process
    #     while queue:
    #         curr_node = queue.popfromleft()
    #         if not curr_node:
    #             continue
    #         idx += 2
    #         left_val = data[idx]
    #         idx += 2
    #         right_val = data[idx]

    #         left_node = create_node(left_val)
    #         right_node = create_node(right_val)

    #         curr_node.left = left_node
    #         curr_node.left = right_node

    #         # update process node
    #         if left_node:
    #             queue.append(left_node)
    #         if right_node:
    #             queue.append(right_node)
            
    #     return root