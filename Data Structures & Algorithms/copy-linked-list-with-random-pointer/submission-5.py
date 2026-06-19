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
        if not head: return head

        # l1.random -> new_node
        # new_node.random -> l1.random

        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.random = l1.random
            l1.random = l2
            l1 = l1.next
        
        # build l2.random
        l1 = head
        ret = l1.random

        while l1:
            l2 = l1.random
            l2.random = l2.random.random if l2.random else None
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next

        return ret