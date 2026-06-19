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

        # build the original ll first
        # along with a dictionary recording old node -> new node
        dummy = Node(0, None)
        dict_node_posn = {}
        
        new_ll = dummy
        curr_build = head

        while curr_build:
            # create new node based on old node
            new_node = Node(curr_build.val, None)
            # record old node -> copied node
            dict_node_posn[curr_build] = new_node
            # add to new ll
            new_ll.next = new_node
            new_ll = new_ll.next
            # update
            curr_build = curr_build.next
        
        # build random
        curr_random = head
        curr_new = dummy.next

        while curr_random:
            if curr_random.random:
                curr_new.random = dict_node_posn[curr_random.random]
            
            curr_random = curr_random.next
            curr_new = curr_new.next
        
        return dummy.next