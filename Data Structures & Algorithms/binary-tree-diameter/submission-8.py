# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # self.ret = 0

        # def dfs(root):
        #     if not root:
        #         return 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     self.ret = max(self.ret, left + right)

        #     return max(left, right) + 1
        
        # dfs(root)
        # return self.ret
        
        ret_diameter = 0

        stack = [root]
        cache = defaultdict(int)

        while stack:
            node = stack[-1]
            if node.left and node.left not in cache:
                stack.append(node.left)
                cache[node.left] = 0
            elif node.right and node.right not in cache:
                stack.append(node.right)
                cache[node.right] = 0
            else:
                # ATP both left, right has been processed
                curr_node = stack.pop()

                left_height = cache[curr_node.left]
                right_height = cache[curr_node.right]

                ret_diameter = max(ret_diameter, left_height + right_height)
                cache[curr_node] = max(left_height, right_height) + 1
        
        return ret_diameter
