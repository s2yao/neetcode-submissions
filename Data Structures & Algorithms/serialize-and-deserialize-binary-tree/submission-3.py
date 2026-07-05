# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Codec:
    
#     # Encodes a tree to a single string.
#     # preorder
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         vals = []

#         def dfs(node):
#             if not node:
#                 vals.append("#")
#                 return
            
#             vals.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)
#         return ",".join(vals)

#     # Decodes your encoded data to tree.
#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         if not data:
#             return None
        
#         data = data.split(',')

#         def create_node(val):
#             if val == "#":
#                 return None
#             else:
#                 return TreeNode(int(val))

#         # global curr_idx
#         self.curr_idx = 0

#         # function that recursively take one subtree
#         # catching left and right
#         def create_tree(root):
#             self.curr_idx += 1
#             if not root:
#                 return None
            
#             left_node = create_tree(create_node(data[self.curr_idx]))
#             right_node = create_tree(create_node(data[self.curr_idx]))
            
#             root.left = left_node
#             root.right = right_node
            
#             return root


#         # make root and
#         # call function
#         return create_tree(create_node(data[self.curr_idx]))




# BFS / level-order version
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"

        vals = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                vals.append("#")
                continue

            vals.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        if vals[0] == "#":
            return None

        root = TreeNode(int(vals[0]))
        queue = deque([root])
        idx = 1

        while queue:
            node = queue.popleft()

            left_val = vals[idx]
            idx += 1
            if left_val != "#":
                node.left = TreeNode(int(left_val))
                queue.append(node.left)

            right_val = vals[idx]
            idx += 1
            if right_val != "#":
                node.right = TreeNode(int(right_val))
                queue.append(node.right)

        return root