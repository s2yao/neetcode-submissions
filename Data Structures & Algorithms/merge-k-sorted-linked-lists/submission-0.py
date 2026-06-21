# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force by linear scan
        dummy_head = ListNode(0)

        # linear scan for each ll of lists
        for ll in lists:
            node = ll
            while node:
                nexter = node.next
                posn_insert = self.look_for_ele(node.val, dummy_head)
                node.next = posn_insert.next
                posn_insert.next = node
                node = nexter

        return dummy_head.next

    
    # dumb linear search of posn to put target
    def look_for_ele(self, target: val, l_list: ListNode) -> ListNode:
        temp = l_list
        while temp.next:
            if temp.next.val >= target:
                break
            temp = temp.next
        # return node that puts target at next 
        return temp