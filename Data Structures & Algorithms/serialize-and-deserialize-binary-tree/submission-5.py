class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def dfs(node):
            if not node:
                values.append("#")
                return

            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        curr_idx = 0

        def dfs():
            nonlocal curr_idx

            value = values[curr_idx]
            curr_idx += 1

            if value == "#":
                return None

            root = TreeNode(int(value))
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()