# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check_same(self, root1, root2):
        stack = [[root1, root2]]
        while stack:
            curr_node1, curr_node2 = stack.pop()
            if not curr_node1 and not curr_node2:
                continue

            if (not curr_node1 and curr_node2) or (curr_node1 and not curr_node2):
                return False

            if curr_node1.val != curr_node2.val:
                return False
            
            stack.append([curr_node1.left, curr_node2.left])
            stack.append([curr_node1.right, curr_node2.right])

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ret = False

        def traversal(curr_node):
            nonlocal ret
            if not curr_node:
                return
            
            if curr_node.val == subRoot.val:
                # print(curr_node.val)
                if self.check_same(curr_node, subRoot):
                    print("why")
                    ret = True
            
            traversal(curr_node.left)
            traversal(curr_node.right)

        traversal(root)
        
        return ret