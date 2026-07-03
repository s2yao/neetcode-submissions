# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serializer(root):
            if not root:
                return "#"
            return str(root.val) + "," + serializer(root.left) + "," + serializer(root.right)
        
        def compare_serialize(root, subroot):
            root_idx = 0
            subroot_idx = 0
            rollback = 0
            while root_idx < len(root) and subroot_idx < len(subroot):
                if root[root_idx] != subroot[subroot_idx]:
                    root_idx += 1
                    continue
                else:
                    rollback = root_idx + 1
                    while subroot_idx < len(subroot) and root_idx < len(root):
                        if root[root_idx] == subroot[subroot_idx]:
                            root_idx += 1
                            subroot_idx += 1
                        else:
                            break
                    if subroot_idx != len(subroot):
                        root_idx = rollback
                        subroot_idx = 0
                    
            
            if subroot_idx == len(subroot):
                return True
            else:
                return False


        serialize_root = serializer(root)
        serialize_subroot = serializer(subRoot)
        
        return compare_serialize(serialize_root, serialize_subroot)

