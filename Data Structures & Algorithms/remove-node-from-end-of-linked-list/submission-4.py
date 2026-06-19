# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the n position first
        ele_posn = head

        while n:
            ele_posn = ele_posn.next
            n -= 1
        
        # ele_posn sits position
        dummy = ListNode(0, head)
        
        left = dummy
        right = ele_posn

        while right:
            right = right.next
            left = left.next
        
        # left.next is element to remove
        left.next = left.next.next
        return dummy.next