# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def dfs(curr_node):
            if not curr_node:
                values.append("#")
                return
            
            values.append(str(curr_node.val))
            dfs(curr_node.left)
            dfs(curr_node.right)

        dfs(root)
        return ",".join(values)

    def create_node(self, val):
        if val == "#":
            return None
        return TreeNode(int(val))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        idx = 0

        def decode():
            nonlocal idx
            
            curr_node = self.create_node(data[idx])
            idx += 1
            if not curr_node:
                return None

            curr_node.left = decode()
            curr_node.right = decode()

            return curr_node

        return decode()
            

        
