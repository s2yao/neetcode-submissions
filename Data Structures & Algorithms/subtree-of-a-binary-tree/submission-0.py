# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the node wiht same val

        # perform dfs compare
        def compare(p, q):
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False
            else:
                left = compare(p.left, q.left)
                right = compare(p.right, q.right)
                return (left and right)

        
        # traverse big tree
        stack = [root]

        while stack:
            curr_node = stack.pop()

            if curr_node.val == subRoot.val:
                if compare(curr_node, subRoot):
                    return True
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
            
        return False