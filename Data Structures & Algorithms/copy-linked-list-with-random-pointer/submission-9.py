"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head

        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.random
            curr.random = new_node
            curr = curr.next
        
        curr = head
        # tackle created node random logic
        while curr:
            created_node = curr.random
            if created_node.next:
                created_node.random = created_node.next.random
            else:
                created_node.random = None
            curr = curr.next

        curr = head
        ret = head.random
        # tackle next logic
        while curr:
            created_node = curr.random
            curr.random = created_node.next
            if curr.next:
                created_node.next = curr.next.random
            else:
                created_node.next = None
            curr = curr.next
        
        return ret